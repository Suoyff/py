import csv
with open('E:\Files\Courses\Semster.2\Machine Learning\ML4MS-week01-python\Homework-1\stockholm.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader) #skip the header
    data = [row for row in reader]

    file_2write = open("E:\Files\Courses\Semster.2\Machine Learning\ML4MS-week01-python\Homework-1\output.csv", 'w')
    writer = csv.writer(file_2write)
    writer.writerow(['Year', 'Month', 'Day', 'T_max', 'T_min', 'T_ave'])

   #Add some variables to facilitate operation
    i=0
    tem_max=-100
    tem_min=100
    data1=[]
#Start with the first data and sort out all the data
    while i<77431:
        j=0
        k=0
        while j < 5:  #Find data with wrong temperature symbol
            if 'a' in data[i][j]  or 'b' in data[i][j]:
                k=k+1
            j = j + 1
        j=0
        if k>0:
            print(data[i])
            while j < 5:   #Remove wrong temperature symbols
                data[i][j] = data[i][j].replace('a', '')
                data[i][j] = data[i][j].replace('b', '')
                j = j + 1
        ave=(float(data[i][3])+float(data[i][4]))/2 #Calculate the daily average temperature
        if ave>tem_max:
            tem_max=ave # Find the highest average temperature
        if ave<tem_min:
            tem_min=ave # Find the lowest average temperature
        data1=data[i]
        data1.append(ave) #Add the daily average temperature to the table
        writer.writerow(data1)
        i = i + 1
    print("Max temperature:",tem_max,"   Min temperature:", tem_min) #Output maximum average temperature and minimum average temperature
    file_2write.close()

    # Plot
    i = 0
    year = []
    year.append(float(data[0][0]))
    ht = -100
    lt = 100
    ss=0
    while i < 77431:
        ave = (float(data[i][3]) + float(data[i][4])) / 2
        if data[i][0]= data[i-1][0]:
            if ht > ave:
                ht=ave
            if lt < ave:
                lt=ave







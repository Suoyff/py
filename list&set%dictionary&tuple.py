# List
# friends = ["John", "Joe", '12345', "David", 'False', ["a", "b", "c"]]
# first, *last, end1 = friends
# friends2=friends.copy() # shallow copy
# friends3=friends #deep copy
# friends3[0]='suo'
# print(friends)
# nums=[1204,99, 417, 528]*2
# friends.remove( ["a", "b", "c"])
# friends.sort()    # 排序    friends.reverse() 翻转
# print(friends)
# friends.extend(nums)
# if 99 in friends:
#     print(friends.index("David"))   #指出坐标
#     print(friends.count(99)) # to cound the number of occurrence
# friends.pop() #remove the last one
# friends.pop(0) #remove the first one  (del friends[0:1] 也是)
#
# friends.append(True)
# print(last*4) # print(*last)
# print(12345 in friends)
# print(friends)

#Dictionary
# contact_1 = {"name": "suoyff", "age":22, "phone": 15237217762, "sex": "male"}
# contact_2 = {"name": "cxr"}
# contact_2["age"]=23
# contact_2["phone"]="19883104177"
# contact_2["sex"]="female"
# print(contact_1)
# print(contact_2)
# print(contact_2["phone"])
# print(contact_2.keys())

#set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
# odds = set([1,3,5,7,9])
# evens = set([2,4,6,8,10])
# primes = {2,3,5,7}
# odds.union(evens)
# odds.intersection(primes)

#tuples are lists but cannot be changed --> immutable
# coordinates = (4, 5) # with parenthesis <--> list with square braket
# coordinates_1= [(4,5), (6, 7), (80, 34)]
# print(coordinates_1[0])


class CK():

  def __init__(self, name):
    self.name = name
  def f(self):
    return float(self.name)+273.15
tem1=input("Enter the Temperature:")
c = CK(tem1)
print("Celsius:",tem1," ℃")
print("Kelvin:",c.f()," K")
class add2:
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def addition(self):
    return self.a+self.b

__nane__='__main__':
number_1=int(input("Enter the first number:"))
number_2=int(input("Enter the second number:))
object32=add2(number_1,number_2)
print(object32.addition)

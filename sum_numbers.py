
#explanation how to raise exeption errors 
#with try expect 


class numbers:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        try:
            return self.a+self.b
        except Exception as e:
            #print(e)
            return 'The both numbers should be of int float or double'
        #finally:
            return "the error is raised"


print("ww")
object32=numbers(int(input()),input())
print("Printing")
print(object32.sum())

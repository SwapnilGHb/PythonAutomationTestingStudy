# Method Overloading

class MathUtils:
    # Method- overloading - Not Supported in python
    def add(self,a = 0,b = 0):
        return a+b

    def add(self,a = 0,b = 0,c = 0):
        return a+b+c

    def add(self,a = 0,b = 0,c = 0,d = 0):
        return a+b+c+d

math = MathUtils()
op1 = math.add(1,2)
print(op1)
op2 = math.add(1,2,3)
print(op2)
op3 = math.add(1,2,3,4)
print(op3)




# Method Overloading is not supported in Python

class Calc:
    def sum(self,*args):
        for a in args:
            print(a)

# *args -> multiple values you can give
calc_ref = Calc()
calc_ref.sum(3,4)
calc_ref.sum(3,4,5)
calc_ref.sum(3,4,5,10)

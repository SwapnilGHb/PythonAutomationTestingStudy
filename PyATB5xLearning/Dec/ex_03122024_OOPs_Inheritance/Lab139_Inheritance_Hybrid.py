# Hybrid Inheritance

# multiple types of Inheritance
# Such as Single
# multiple, and
# multilevel inheritanceA

class A:  # Father
    def methodA(self):
        return "MethodA"

class B(A):  # Pramod
    def methodB(self):
        return "MethodB"

class C(A):  # Lucky
        def methodC(self):
            return "MethodC"

class D(B,C):  # Sister Multiple,Multilevel
    def methodC(self):
        return "MethodD"

d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())

# Hirarchical Inheritance

class Father:

    def BHK1(self):
        print("BHK1")

class Pramod(Father):
    def BHK2(self):
        print("BHK2")

class Amit(Father):
    def BHK3(self):
        print("BHK3")

class Lucky(Father):
    def no_house(self):
       print("No House")

pramod = Pramod()
pramod.BHK1()
pramod.BHK2()

amit = Amit()
amit.BHK3()
amit.BHK1()

l = Lucky()
l.no_house()
l.BHK1()
class Parent:
    gold = "2kg"

    def __init__(self):
        print("DC - Parent")

    def BHK2(self):
        print("2BHK")

class Child(Parent):
    def __init__(self):
        print("DC - Child")
    diamond = "Diamond"

    def BHK3(self):
        print("3BHK")

child_obj = Child()
print(child_obj.gold)
child_obj.BHK2()

father_obj_ref = Parent()
father_obj_ref.BHK2()
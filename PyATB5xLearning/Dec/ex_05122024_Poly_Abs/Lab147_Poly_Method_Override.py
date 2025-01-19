class Parent:
    def home(self):
        print("2BHK")

class Son(Parent):
    def town(self):
        print("5BHK")

    def home(self):
        print("3BHK")

obj_ref = Son()
obj_ref.home()
obj_ref.town()
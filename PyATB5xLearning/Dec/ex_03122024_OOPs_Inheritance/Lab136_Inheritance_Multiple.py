# Multiple Inheritance

class Father:

    def home(self):
        return "This is from Father"

    def father_money(self):
        return 5


class Mother:

    def home(self):
        return "This is from Mother"

    def mother_money(self):
        return 2

class Son(Father, Mother): # Multiple Inheritance
    def print_info(self):
        print("Son has father and mother money",)

s = Son()
print(s.father_money())
print(s.mother_money())
print(s.home())
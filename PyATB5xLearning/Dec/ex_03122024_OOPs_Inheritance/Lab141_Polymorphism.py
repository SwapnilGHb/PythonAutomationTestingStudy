# Method Overloading

class Dog:
    def bark(self,breed=None):
        return breed
        print('Dog is barking')

    def bark(self,breed):  # Only the latest defined method get invoked.
        print(f'Dog with {breed} is barking')

d = Dog()

d.bark()
d.bark()


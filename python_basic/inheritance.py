# Inheritance

# Inheritance is a technique to remove code duplication. We can create a base class
# to define the common methods and then have other classes inherit these methods.

class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    def bark(self):
        print('brak')

dog = Dog()
dog.walk() # inherited from Mammal
dog.bark() # defined in Dog
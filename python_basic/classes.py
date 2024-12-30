# Classes 
# We use classes to define new types

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
point1 = Point(1,2)
print(point1.x)
# When a function is part of a class, we refer to it as a method.

# Classes define templates or blueprints for creating objects. An object is an instance
# of a class. Every time we create a new instance, that instance follows the structure
# we define using the class.
point1 = Point(10, 5)
point2 = Point(2, 4)
# __init__ is a special method called constructor. It gets called at the time of
# creating new objects. We use it to initialize our objects.
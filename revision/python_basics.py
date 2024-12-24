# Variables and Data Types

# Number
num = 10       # int
price = 19.99  # float

# String
greeting = "Hello, World!"

# Boolean
is_active = True

# None (equivalent to null in JavaScript)
nothing = None

# Lists (Similar to Arrays in js.....) & are ordered, mutable, and can hold elements of different types

fruits =['apple','banana','cherry']
print(fruits[0]) # Output: apple
fruits.append('orange') # Add an element & common list methods remove(), pop(), sort()....
print(len(fruits)) # Output: 4

# Tuples (are immutable ordered collections)
coordinates = (10,20)
print(coordinates[0]) # Output: 10
# coordinates[0] = 30  # Error: Tuples are immutable


# Dictionaries (Similar to Object in Js) and store key-value pairs

person={
    "name":"Alice",
    "age":25,
    "city":"NY"
}
print(person["name"]) # Output: Alice
person['age'] = 26 # Update value

# Control Structures,  If-Else Statements
age = 18
if age >= 18:
    print('Adult')
else:
    print('Minor')

# Loops 
# for in loop
fruits2 =['apple','banana','cherry']
for fruit in fruits2:
    print(fruit) # Output: apple banana cherry

# while loops
count = 0
while count < 3:
    print(count) # Output: 0 1 2 
    count += 1 

# Functions
def greet(name):
    return f"Hello, {name}"
print(greet('Alice')) # Output: Hello, Alice

# Arrow Function Equivalent
square = lambda x: x * x
print(square(5)) # Output: 25

# Classes and Objects
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."
person = Person("Alice", 25)
print(person.greet()) # Output: My name is Alice.

# Common Data Structures 

# Sets  Unordered collections of unique elements.
numbers = {1, 2, 3, 3}
print(numbers)  # Output: {1, 2, 3}

# Lists (Arrays) Ordered collections.
nums = [1, 2, 3, 4]

# Tuples Immutable sequences.
immutable_data = (10, 20)

# Dictionaries Key-value pairs.
data = {"key": "value"}

# Modules
import math
print(math.sqrt(16))  # Output: 4.0

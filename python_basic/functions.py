# Functions 

# We use functions to breake up our code in to small chunks. These chunks are easier 
# to read, understand and maintain. If there are bug, it's easier to find bugs ina small
# chunk than the entire program. We can also re-use these chunks.
def greet_user(name):
    print(f"Hi {name}")

greet_user('John')

# Parameters:  are a placeholders for the data we can pass to functions.  def greet_user(name)
# Arguments: are the actual values we pass like => greet_user('John')

# • Positional arguments: their position (order) matters
# • Keyword arguments: position doesn’t matter - we prefix them with the parametername.

# Two positional arguments
greet_user('John', 'Smith')

# Keyword arguments
calculate_total(order=50,shipping=5,tax=0.1)

# Our functions can return values. if we don't use the return statement, by default
# (None) is returned. Node is an obj that represents the absence of a value

def square(number):
    return number * number
result = square(2)
print(result)
# Exceptions are errors that crash our programs. They often happen because of bad input or programming errors.
# It’s our job to anticipate and handle these exceptions to prevent our programs from cashing.

# example-1
try:
    age = int(input("Age: "))
    if age < 0:
        raise ValueError("Age cannot be less than 0.")
    elif age > 110:
        raise ValueError("Age cannot be greater than 110.")
    else:
        print("Your age is:", age)
except ValueError as ex:
    print(ex)

# example-2
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Not a valid number.")
except ZeroDivisionError:
    print("Age cannot be 0.")
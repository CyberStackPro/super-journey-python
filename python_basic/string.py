# Strings
# We can define strings using single (‘ ‘) or double (“ “) quotes.
# To define a multi-line string, we surround our string with tripe quotes (“””).

course = 'Python for Beginners'
course[0] # returns the first character
course[1] # returns the second character
course[-1] # returns the first character from the end
course[-2] # returns the second character from the end

# Slicing string

print(course[1:5])

name = 'John'
message = f"Hi my name is {name}"
message.upper()# to convert to uppercase
message.lower()# to convert to lowercase
message.title()# to capitalize the first letter of every word
message.find('p') # returns the index of the first occurrence of p (or -1 if not found)
message.replace('p', 'q')

# To check if a string contains a character (or a sequence of characters), we use the inoperator:
contains = 'Python' in course
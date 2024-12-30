# Lists

numbers = [1,2,3,4,5]

numbers[0] # returns the first item
numbers[1] # returns the second item
numbers[-1] # returns the first item from the end
numbers[-2] # returns the second item from the end

numbers.append(6) # adds 6 to the end
numbers.insert(0,6) # adds 6 at index position of 0
numbers.remove(6) # removes 6 at the first postion
numbers.pop() # removes the last item
# numbers.clear() # removes all the items
numbers.index(8) # returns the index of first occurrence of 8
numbers.sort() # sorts the list
numbers.reverse() # revers the list
numbers.copy() # returns a copy of the list

print(numbers)
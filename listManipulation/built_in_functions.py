# There are many built in functions for Lists: 

# len()
example_list = [1,"test","one"]
print("Length Function:", len(example_list))

#examples
"""
 len(sequence) returns the length (number of items) in a sequence.
 max(sequence) returns the highest value in a sequence.
 min(sequence) returns the lowest value in a sequence.
 sorted(sequence) returns a sorted sequence
"""
numList = [1,3,8,5,12,2]
print(min(numList))
print(sorted(numList))

# .pop()
numList.pop()
print(numList)

# .index(): returns index position
print(numList.index(8))

# .sort()
print(numList.sort())
print(numList)

"""
list.append(value) appends a value to the end of the list.
list.pop(index) remove a value at given position. if no parameter is passed, it will remove the last value in the list.
list.index(value) returns the index (position) of the given value if it exists in the list and raises an error if it does not exist.
list.reverse() reverses the order of the elements, in place.*
list.sort() sorts the items in order of least to greatest, or alphabetically for strings, in place.*
"""
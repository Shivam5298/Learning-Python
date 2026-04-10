# This is a simple program that demonstrates the use of lists in Python.
# A list is a collection of items that are ordered and changeable.

exampleList1 = [5, 10, 15, 20, 25]
exampleList2 = [1.1, 1.2, 1.3, 1.4, 1.5] 
exampleList3 = ["apple", "banana", "cherry", "date", "elderberry"]
exampleList4 = [True, False, True, False, True]
exampleList5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
exampleList6 = [5, "apple", True, 1.1, [1, 2, 3]]

# We can access individual items in a list using their index.

# The list() function can be used to create a list from an iterable.    
# For example, we can create a list from a string:

exampleString = "Hello, World!"
exampleList7 = list(exampleString)

# We can also create a list from a range of numbers:

exampleList8 = list(range(1, 11))

# We can also create a list from a tuple:
exampleTuple = (1,(1,2), 3, 4, 5)
exampleList9 = list(exampleTuple)
print(exampleList9)

# We can also create a list from a set:
exampleSet = {1, 2, 3, 4, 5}
exampleList10 = list(exampleSet)
print(exampleList10)

# The in keyword can be used to check if an item is in a list:
print(10 in exampleList1)  # True
print(1.1 in exampleList2)  # True
print("Grapes" in exampleList3)  # False

# The not in keyword can be used to check if an item is not in a list:
print(30 not in exampleList1)  # True
print(1.6 not in exampleList2)  # True
print("banana" not in exampleList3)  # False

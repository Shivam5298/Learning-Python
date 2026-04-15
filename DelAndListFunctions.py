#This is a sample program that demonstrates the use of the del statement and list functions in Python.  
# The del statement is used to delete items from a list.
exampleList = [1, 2, 3, 4, 5]
# We can use the del statement to delete an item from a list by its index.
print("Before deletion:", exampleList)
del exampleList[2]  # This will delete the item at index 2 (the number 3)
print("After deletion:", exampleList)

# We can also use the del statement to delete a slice of items from a list.
exampleList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Before deletion:", exampleList2)
del exampleList2[2:5]  # This will delete the items at index 2, 3, and 4 (the numbers 3, 4, and 5)
print("After deletion:", exampleList2)

# We can also use the del statement to delete an entire list.
exampleList3 = [1, 2, 3, 4, 5]
print("Before deletion:", exampleList3)
del exampleList3  # This will delete the entire list
# print("After deletion:", exampleList3)  # This will raise an error because the list has been deleted

# We can use the len() function to get the length of a list.
exampleList4 = [1, 2, 3, 4, 5]
print("Length of exampleList4:", len(exampleList4))

# We can use the max() function to get the maximum value in a list.
print("Maximum value in exampleList4:", max(exampleList4))

# We can use the min() function to get the minimum value in a list.
print("Minimum value in exampleList4:", min(exampleList4))

# Remove() function is used to remove the first occurrence of a specified value from a list.
exampleList5 = [1, 2, 3, 4, 5, 2]
print("Before removal:", exampleList5)
exampleList5.remove(2)  # This will remove the first occurrence of the number 2
print("After removal:", exampleList5)

# append() function is used to add an item to the end of a list.
exampleList6 = [1, 2, 3, 4, 5]
print("Before appending:", exampleList6)
exampleList6.append(6)  # This will add the number 6 to the end of the list
print("After appending:", exampleList6)

# insert() function is used to add an item at a specified index in a list.
exampleList7 = [1, 2, 3, 4, 5]
print("Before inserting:", exampleList7)
exampleList7.insert(2, 6)  # This will insert the number 6 at index 2
print("After inserting:", exampleList7)

# sort() function is used to sort the items in a list in ascending order.
# If you want to sort in descending order, you can use the reverse parameter.
# sort only works on lists that contain items of the same type (e.g., all numbers or all strings).
exampleList8 = [5, 2, 9, 1, 5, 6]
print("Before sorting:", exampleList8)
exampleList8.sort()  # This will sort the list in ascending order
print("After sorting:", exampleList8)
# If you want to sort in descending order, you can use the reverse parameter.
exampleList8.sort(reverse=True)  # This will sort the list in descending order
print("After sorting in descending order:", exampleList8)
exampleList9 = ["banana", "apple", "cherry", "date"]
print("Before sorting:", exampleList9)
exampleList9.sort()  # This will sort the list in alphabetical order
print("After sorting:", exampleList9)

# pop() function is used to remove and return an item from a list at a specified index.
exampleList10 = [1, 2, 3, 4, 5]
print("Before popping:", exampleList10)
poppedItem = exampleList10.pop(2)  # This will remove and return the item at index 2 (the number 3)
print("Popped item:", poppedItem)
print("After popping:", exampleList10)


artic_animals = ["penguin", "elephant", "polar bear", "walrus","tiger","reindeer"]

print("Before Manipulation",artic_animals)

# Removing tiger from list using del

del artic_animals[4]

# Remove elephant from list using remove()
artic_animals.remove("elephant")

# Use append to add artic fox to list
artic_animals.append("artic fox")

# Use insert to insert snowy owl between polar bear and walrus
artic_animals.insert(2, "snowy owl")

print("After Manipulation", artic_animals)

# Index of reindeer in artic_animals
index = artic_animals.index("reindeer")
print(index)

# Use pop to get the last item from the list and print it
last_item = artic_animals.pop()
print(last_item)
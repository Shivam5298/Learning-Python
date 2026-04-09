mixedCase = "A Song of Ice and Fire"

# check if all characters in the string are uppercase

print(mixedCase.isupper())

# check if all characters in the string are lowercase

print(mixedCase.islower())

# change the string to uppercase

print(mixedCase.upper())

# change the string to lowercase

print(mixedCase.lower())

# check if the string is title case

print(mixedCase.istitle())

# create a new string in title case

titleCase = mixedCase.title()
print(titleCase)

# check starts with

print(mixedCase.startswith("A"))

# check ends with
print(mixedCase.endswith("e"))

# split the string into a list of words
words = mixedCase.split(" ")
print(words)

# join the list of words back into a string

joinedString = " ".join(words)
print(joinedString.isalpha())

print(joinedString)


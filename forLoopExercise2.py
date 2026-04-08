string = input("Enter a string: ")

numberOfCharacters = 0

for letter in string:
    numberOfCharacters += 1

print("Entered string was: ",string)
print("The number of characters in the entered string is: ",numberOfCharacters)
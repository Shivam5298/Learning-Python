# This is a program that takes a string input from the user and reverses it.

string = input("Enter a string to reverse: ")

reversedString = ""

for i in string:
    reversedString = i + reversedString

print("Reversed string:", reversedString)
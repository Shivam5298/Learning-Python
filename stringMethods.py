sampleString = "Hello, World!"

# String Methods

# 1. upper() - Converts a string to uppercase

print(sampleString.upper())  # Output: "HELLO, WORLD!"

# 2. lower() - Converts a string to lowercase

print(sampleString.lower())  # Output: "hello, world!"

# 3. isUpper() - Checks if all characters in the string are uppercase

print("Contains Mix of Cases".isupper())  # Output: False
print("all lowercase".isupper())  # Output: False
print("ALL UPPERCASE".isupper())  # Output: True

# 4. isLower() - Checks if all characters in the string are lowercase
print("Contains Mix of Cases".islower())  # Output: False
print("all lowercase".islower())  # Output: True    
print("ALL UPPERCASE".islower())  # Output: False   

# 5. isalpha() - Checks if all characters in the string are alphabetic
print("HelloWorld".isalpha())  # Output: True
print("Hello World".isalpha())  # Output: False (space is not alphabetic)
print("Hello123".isalpha())  # Output: False (numbers are not alphabetic)

# 6. isalnum() - Checks if all characters in the string are alphanumeric
print("Hello123".isalnum())  # Output: True
print("Hello World".isalnum())  # Output: False (space is not alphanumeric)
print("Hello!".isalnum())  # Output: False (exclamation mark is not alphanumeric)

# 7. isdecimal() - Checks if all characters in the string are decimal characters
print("12345".isdecimal())  # Output: True
print("123.45".isdecimal())  # Output: False (period is not a decimal character)
print("Hello123".isdecimal())  # Output: False (letters are not decimal characters)

# 8. isspace() - Checks if all characters in the string are whitespace
print("   ".isspace())  # Output: True
print("Hello World".isspace())  # Output: False 
print("".isspace())  # Output: False (empty string is not considered whitespace)

# 9. title() - Converts the first character of each word to uppercase and the rest to lowercase
print("hello world".title())  # Output: "Hello World"
print("PYTHON programming".title())  # Output: "Python Programming"

# 10. strip() - Removes leading and trailing whitespace from the string
print("   Hello, World!   ".strip())  # Output: "Hello, World!"
print("   Hello, World!   ".lstrip())  # Output: "Hello, World!   " (removes leading whitespace)
print("   Hello, World!   ".rstrip())  # Output: "   Hello, World!" (removes trailing whitespace)

# istitle() - Checks if the string is in title case
print("Hello World".istitle())  # Output: True
print("hello world".istitle())  # Output: False
print("Hello world".istitle())  # Output: False (only the first word is capitalized)

# 11. replace() - Replaces occurrences of a specified substring with another substring
print("Hello, World!".replace("World", "Python"))  # Output: "Hello, Python!"
print("banana".replace("a", "o"))  # Output: "bonono"

# 12. split() - Splits a string into a list of substrings based on a specified delimiter
print("Hello, World!".split(", "))  # Output: ['Hello', 'World!']
print("one,two,three".split(","))  # Output: ['one', 'two', 'three']

# 13. join() - Joins a list of strings into a single string with a specified delimiter
words = ["Hello", "World"]
print(" ".join(words))  # Output: "Hello World"
print("-".join(words))  # Output: "Hello-World"

# 14. find() - Returns the lowest index of the substring if found, otherwise returns -1
print("Hello, World!".find("World"))  # Output: 7
print("Hello, World!".find("Python"))  # Output: -1 (not found)

# 15. count() - Returns the number of occurrences of a substring in the string
print("banana".count("a"))  # Output: 3
print("banana".count("na"))  # Output: 2

# 16. startswith() - Checks if the string starts with a specified substring
print("Hello, World!".startswith("Hello"))  # Output: True
print("Hello, World!".startswith("World"))  # Output: False

# 17. endswith() - Checks if the string ends with a specified substring
print("Hello, World!".endswith("!"))  # Output: True
print("Hello, World!".endswith("World"))  # Output: False

# 18. len() - Returns the length of the string
print(len(sampleString))  # Output: 13

# 19. format() - Formats a string using placeholders
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

# 20. f-strings - A more concise way to format strings (available in Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# 21. ord() - Returns the Unicode code point of a character
print(ord('A'))  # Output: 65
print(ord('a'))  # Output: 97

# 22. chr() - Returns the character corresponding to a Unicode code point
print(chr(65))  # Output: 'A'
print(chr(97))  # Output: 'a'

# 23. isdigit() - Checks if all characters in the string are digits
print("12345".isdigit())  # Output: True
print("123.45".isdigit())  # Output: False (period is not a digit)
print("Hello123".isdigit())  # Output: False (letters are not digits)

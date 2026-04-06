# int() and float() functions are used to convert values to integers and floating-point numbers, respectively.
# The int() function can be used to convert a string or a floating-point number to an integer.
# The float() function can be used to convert a string or an integer to a floating-point

userInput = input("Enter a number: ")
print("Entered value as string:", userInput)
print(type(userInput))

# Convert the input to an integer
int(userInput)
print("Entered value as integer:", int(userInput))
print(type(int(userInput)))

# Convert the input to a floating-point number
print("Now converting the input to a floating-point number")
var1 = input("Enter a number: ")
print("Entered value as string:", var1)
print(type(var1))

# Convert the input to a floating-point number
float(var1)
print("Entered value as floating-point number:", float(var1))
print(type(float(var1)))

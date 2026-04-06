# A sample program demonstrating the use of functions in Python

def hello():
    print("Hello, World!")


hello()

def greet():
    name = input("Enter your name: ")
    print("Hello, " + name + "!")


greet()

#Functions can also take parameters and return values

def multiply(num1, num2):
    print(num1 * num2)


multiply(10,2)

# The return statement is used to return a value from a function.

def add(num1, num2):
    return num1 + num2


result = add(5, 3)
print("The sum is:", result)    

# We can also use the return value directly without storing it in a variable.
# For example, we can print the result of the add function directly:

print("The sum is:", add(10, 20))

# We can aslo assign default values to parameters in a function. This allows us to call the function without providing arguments for those parameters.

def sum(num1 = 10, num2 = 20):
    return num1 + num2

print("The sum is:", sum())  # This will use the default values of num1 and num2
print("The sum is:", sum(5, 15))  # This will override the default values with 5 and 15
print("The sum is:", sum(5))  # This will override the default value of num1 with 5 and use the default value of num2 (20)
print("The sum is:", sum(num2 = 30))  # This will override the default value of num2 with 30 and use the default value of num1 (10)

# we can also call a function from another function. This is known as nested functions.

def outer_function():
    print("This is the outer function.")
    hello()  # Calling the hello function from the outer_function
    multiply(sum(5, 10), 2)  # Calling the sum function and passing its result to the multiply function
    print("This is the end of the outer function.")


outer_function()
# This is a sample code to demonstrate the use of if statements in Python
# An if statement is used to test a condition. If the condition is true.
# The code  block inside the if statement will be executed. If the condition is false, the code block will be skipped.

# Example of using an if statement

name = "Shivam"

if name == "Shivam":
    print("Hello, Shivam! Welcome to Python programming.")

# Example of using an if statement with a different condition
age = 25
if age >= 18:
    print("You are an adult.")

# Example of using an if statement with a false condition

temperature = 30
if temperature < 20:
    print("It's a cold day.")

# Example of using an if statement with an else clause

score = 85
if score >= 90:
    print("You got an A!")
else:
    print("You did not get an A.")

# Example of using an if statement with an elif clause

grade = 85

if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C!")
elif grade >= 60:
    print("You got a D.")
elif grade < 50:
    print("You got an E.")
else:
    print("You failed the exam.")       

# Example of using nested if statements
number = 10 
if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else: 
    print("The number is not positive.")



# This program demonstrates the use of the range() function in Python.
# The range() function generates a sequence of numbers, which can be used in for loops.

num = range(5) # This will generate a sequence of numbers from 0 to 4 (5 is not included)

for i in num: 
    print(i) # This will print the numbers from 0 to 4, each on a new line

# We can also specify a starting point and an end value in the range() function.
# This can be done by passing two arguments to the range() function.

num2 = range(5 , 10) # This will generate a sequence of numbers from 5 to 9 (10 is not included)

for i in num2: 
    print(i) # This will print the numbers from 5 to 9, each on a new line

# We can also specify a step value in the range() function.
# This can be done by passing three arguments to the range() function.

num3 = range(10, 21, 2) # This will generate a sequence of numbers from 10 to 20 (21 is not included) with a step of 2
for i in num3: 
    print(i) # This will print the numbers 10, 12, 14, 16, 18, and 20, each on a new line
    
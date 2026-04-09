# This is a simple program to calculate the factorial of a number

num = int(input("Enter a number to calculate its factorial: "))
counter = 1
factorial = 1

while counter >= 1 and counter <= num: 
    factorial *= counter
    counter +=1

print("The factorial of ",num," is ",factorial)
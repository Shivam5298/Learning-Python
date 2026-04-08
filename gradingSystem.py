# This is a program to demonstrate a grading system using if statements in Python
# The program will take a score as input and will output the corresponding grade based on the score 

score = int(input("Enter your score: "))

if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")   
elif score >= 70:
    print("You got a C!")
elif score >= 60:
    print("You got a D.")
else:
    print("You failed the exam.")


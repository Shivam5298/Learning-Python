# This is a program to convert an integer to a Roman numeral using if statements in Python
# The program will take an integer as input and will output the corresponding Roman numeral based on the integer

num = int(input("Enter an Integer between 1 and 10: "))

if num == 1:
    print("1 in roman numerals is I")
elif num == 2:
    print("2 in roman numerals is II")
elif num == 3:
    print("3 in roman numerals is III")
elif num == 4:
    print("4 in roman numerals is IV")
elif num == 5:
    print("5 in roman numerals is V")
elif num == 6:
    print("6 in roman numerals is VI")
elif num == 7:
    print("7 in roman numerals is VII")
elif num == 8:
    print("8 in roman numerals is VIII")
elif num == 9:
    print("9 in roman numerals is IX")
elif num == 10:
    print("10 in roman numerals is X")
else: 
    print("The entered number is either a whole number or not between 1 and 10")
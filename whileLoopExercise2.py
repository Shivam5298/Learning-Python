num = int(input("Enter a number between 1 and 10: "))

sum = 0

if num <= 0 or num >=10:
    print("Enter a number in the given range")
else:
    while num != 0: 
        sum = sum + num
        num -=1

print(sum)


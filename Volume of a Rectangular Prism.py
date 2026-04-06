# This is a program that calculates the volume of a rectangular prism.

length = float(input("Enter the length of the rectangular prism: "))
width = float(input("Enter the width of the rectangular prism: "))
height = float(input("Enter the height of the rectangular prism: "))

def calcVolume(length, width, height):
    volume = length * width * height
    print("The volume of the rectangular prism is: ",volume)


calcVolume(length, width, height)
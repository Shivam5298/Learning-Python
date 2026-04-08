import math
import random

# This will generate a random integer between 10 and 25, representing the gallons of fuel you have.
fuel = random.randint(10,25) 


# This will generate a random integer between 200 and 400, representing the distance you can travel with the fuel you have.
distance = random.randint(200,400) 

# This will calculate the miles per gallon by dividing the distance by the fuel and rounding it to 2 decimal places.
miles_per_gallon = round(distance / fuel, 2) 

print("You have ",fuel,"gallons of fuel and you can travel",distance," miles.")
print("Your miles per gallon is:", miles_per_gallon)

print("The car can travel", distance//fuel, "miles with the fuel you have.")

# This is a program to convert Farenheit to Celcius

farenheit = float(input("Enter the temperature in Farenheit: "))

def calcFarenheitToCelsius(farenheit):
    celsius = round((farenheit - 32) * 5.0/9.0, 2)
    return celsius

print("The temperature in Celcius is: ", str(calcFarenheitToCelsius(farenheit)))


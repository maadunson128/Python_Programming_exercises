###program: To calculate cost per square inch
import math
def calculate(diameter, price):
    radius = diameter / 2
    area =  math.pi * (radius **2)  
    cost_per_inch = price / area
    print("Cost per square inch:", cost_per_inch,'rupees')

diameter = float(input("Enter the diameter of pizza in inches: "))
price = float(input("Enter the cost of the pizza: "))

calculate(diameter, price)

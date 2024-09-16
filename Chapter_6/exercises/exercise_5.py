###Program: Area of pizza and cost per inch

import math
#function for calculating area of pizza
def calculate_area(radius:float)->float:
    return math.pi * math.pow(radius, 2)

#function to calculate the cost of pizza per inch
def calculate_cost_inch(cost, area)->float:
    return cost / float(area)

def main()->None:

    #cost, diameter input from the user
    diameter = float(input("Enter the diameter of the pizza in inches: "))
    cost = float(input("Enter the cost of the pizza in rupees: "))

    #calculating area and cost per inch
    area = calculate_area(diameter/2)
    cost_inch = calculate_cost_inch(cost, area)

    print(f"The area of pizza: {area:.3f} sq.inches \n The cost of pizza per inch : {cost_inch:.3f}rupees")


main()
    

    

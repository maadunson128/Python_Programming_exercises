###Program: To calculate volume and surface area
import math

def calculate(radius):
    volume = 4/3 * math.pi * (radius ** 3)
    surface_area = 4 * math.pi * (radius **2)
    print("Volume of sphere:",volume, "cubic units")
    print("Surface area:", surface_area,"sq units")

radius = float(input("Enter the radius: "))
calculate(radius)
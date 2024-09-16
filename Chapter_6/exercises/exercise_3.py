##Program: Surface area and volume of sphere

#importing modules
import math

#function for surface area of sphere
def calculate_surface_area(radius)->float:
    return 4 * math.pi * math.pow(radius, 2)

#function for volume of sphere
def calulate_volume(radius)->float:
    return (4/3) * math.pi * math.pow(radius, 3)

def main()->None:

    #input from the user -> radius
    radius = float(input("Enter the radius of the sphere: "))

    #calulating the surface area and volume
    surface_area = calculate_surface_area(radius)
    volume = calulate_volume(radius)

    print(f"Surface area of sphere: {surface_area:.5f}sq.units \nVolume of sphere: {volume:.5f}cub.units")


main()

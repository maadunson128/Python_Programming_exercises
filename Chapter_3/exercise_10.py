#Program: To find the length of the ladder

import math
def find_length(height, angle):
    angle = (math.pi / 180 ) * angle
    length = height / math.sin(angle)
    print("The length of ladder:", length, "units")

height = float((input("Enter the height of the house/building: ")))
angle = float(input("Enter the angles in degrees: "))

find_length(angle=angle, height=height)

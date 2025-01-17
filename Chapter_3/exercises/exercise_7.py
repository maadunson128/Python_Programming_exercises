#Program: Distance between two points
import math

def find_distance(x1, x2, y1, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) **2 )
    print(f"The distance between points ({x1, y1}) and ({x2, y2}): {distance}")


x1, y1 = eval(input("Enter the point 1 values (x1, y1) separated by commas: "))
x2, y2 = eval(input("Enter the point 2 values (x2, y2) separated by commas: "))

find_distance(x1, x2, y1, y2)

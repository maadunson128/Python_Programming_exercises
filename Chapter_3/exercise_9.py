#Program: To find area of triangle

import math

def find_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print("The area of triangle:", area, "sq.units")

a = eval(input("Enter the side a: "))
b = eval(input("Enter the side b: "))
c = eval(input("Enter the side c: "))

find_area(a, b, c)
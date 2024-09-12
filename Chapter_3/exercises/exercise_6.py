###Program: To find the slope of two non linear points

def find_slope(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    print(f"Slope of points ({x1, y1}) and ({x2, y2}) : {slope}")

print("Note: The points going to be entered must be non-linear points.")
x1, y1 = eval(input("Enter the point 1 values (x1, y1) separated by commas: "))
x2, y2 = eval(input("Enter the Point 2 (x2, y2) separated by commas: "))

find_slope(x1, x2, y1, y2)
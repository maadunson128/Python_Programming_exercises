###Program: Area of triangle

#importing modules
from graphics import *
import math

#function for calculating the area of traingle
def calculate_area_triangle(a:float, b:float, c:float)->float:
    side:float = (a + b + c)/float(2)
    print(side, a, b, c)
    area = math.sqrt(side * (side-a) * (side-b) * (side-c))
    return area


#function for calculating the vertices length
def calculate_length(p1, p2)->float:
    x1, x2, y1, y2 = p1.getX(), p2.getX(), p1.getY(), p2.getY()
    length = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))
    return length

def display_triangle()->None:

    #creating window
    win = GraphWin("Triangle", 600, 400)
    win.setCoords(0.0, 0.0, 10, 10)

    #message
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    #Get and draw the vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    #drawing the triangle using polygon object
    triangle = Polygon(p1, p2, p3)
    triangle.setFill('cyan')
    triangle.setOutline('blue')
    triangle.draw(win)

    #Displaying the area of triangle
    a = calculate_length(p1, p2)
    b = calculate_length(p2, p3)
    c = calculate_length(p1, p3)
    area = calculate_area_triangle(a, b, c)
    
    #Displaying the area of triangle
    message.setText(f'The area of triangle : {area:.4f} sq.units')


    win.getMouse()
    win.close()


display_triangle()

###Program: Rectangle with area and perimeter

from graphics import *
import math

def main():
    win = GraphWin('Rectangle', 700, 700)

    #Getting co-ords from the user input
    pt1 = win.getMouse()
    pt2 = win.getMouse()

    rect = Rectangle(pt1, pt2)
    rect.draw(win)


    #Rectangle parameters/properties
    length = abs(pt1.getX() - pt2.getX())
    breadth = abs(pt1.getY() - pt2.getY())

    area = length * breadth
    perimeter = 2 * (length + breadth)

    Text(Point(500, 500), f'Area: {area}sq.units').draw(win)
    Text(Point(500, 600), f'Perimeter: {perimeter}units').draw(win)


    input()
    win.close()


main()



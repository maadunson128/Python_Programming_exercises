###Program: Drwaing a triangle and displaying its area.

from graphics import *
import math

def main():
    win = GraphWin('Triangle Visualisation', 700, 700)

    #Getting Triangle vertices points
    pt1 = win.getMouse()
    pt2 = win.getMouse()
    pt3 = win.getMouse()

    Polygon(pt1, pt2, pt3).draw(win)

    dx1 = abs(pt1.getX() - pt2.getX())
    dy1 = abs(pt1.getX() - pt2.getY())
    a = math.sqrt((dx1**2) + (dy1**2))

    dx2 = abs(pt2.getX() - pt3.getX())
    dy2 = abs(pt2.getX() - pt3.getY())
    b = math.sqrt((dx2**2) + (dy2**2))

    dx3 = abs(pt1.getX() - pt3.getX())
    dy3 = abs(pt1.getX() - pt3.getY())
    c = math.sqrt((dx3**2) + (dy3**2))


    s = (a + b + c) /2
    area = s * (s+1) * (s+2)

    Text(Point(350, 600), f'Area: {area}sq.units').draw(win)

    input()
    win.close()

main()



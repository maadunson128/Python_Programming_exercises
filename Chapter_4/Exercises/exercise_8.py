###Program: Drawing line segment

from graphics import *
import math

def main():
    win = GraphWin('Line segment', 700, 700)
    win.setCoords(0, 0, 10, 10)
    x = win.getMouse()
    x1 = x.getX()
    y1 = x.getY()

    y = win.getMouse()
    x2 = y.getX()
    y2 = y.getY()

    midpointx = (x1 + x2) / 2
    midpointy = (y1 + y2) / 2

    p = Circle(Point(midpointx, midpointy), 0.05)
    p.setFill('cyan')
    p.draw(win)

    line = Line(Point(x1, y1), Point(x2, y2))
    line.setFill('black')
    line.draw(win)

    #Finding slope
    dx = x2 - x1
    dy = y2 - y1


    slope = dx/dy
    length = math.sqrt((dx**2) + (dy **2))

    #Displaying the length and slope
    Text(Point(6, 3), f'Slope: {slope}').draw(win)
    Text(Point(6, 2), f'Length of line: {length}').draw(win)


    input()
    win.close()

main()
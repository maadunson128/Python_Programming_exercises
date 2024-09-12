###Program: Displaying the co-ordinates where the mouse clicked.

from graphics import *

win = GraphWin("Click me!", 1000, 1000)

for i in range(12):
    p = win.getMouse()
    print("You clicked at: ", p.getX, p.getY)



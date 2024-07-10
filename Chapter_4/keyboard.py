###Program: Keyboard interaction in Graphical module

from graphics import *

win = GraphWin("Keyboard interaction", 500, 500)
p = win.getMouse()
m = win.getKey()

label = Text(p, m)
label.draw(win)

input("Enter any key")
win.close()
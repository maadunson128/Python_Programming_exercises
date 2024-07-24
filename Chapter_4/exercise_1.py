#Program : Modififcation of Discussion problem

from graphics import *

def main():
    win = GraphWin()
    #Creating the default rectangle
    rect = Rectangle(Point(50, 60), Point(80, 90))
    rect.setFill("green")
    rect.setOutline("black")
    rect.draw(win)
    c = rect.getCenter()
    
    #Drawing rectangles where we are clicking.
    for i in range(10):
        p = win.getMouse()

        dx = p.getX() - c.getX()
        dy = p.getY() - c.getX()
        newrect = Rectangle(Point(50 + dx, 60 + dy), Point(80 + dx, 90 + dy))
        newrect.setFill("green")
        newrect.setOutline("black")
        newrect.draw(win)

    #Text message for exit.
    text = Text(Point(100, 20), "Click again to exit.")
    text.draw(win)
    win.getMouse()
    win.close()

    input("")


main()

# Program : Drawing a Archery target
# Draw the circle from Outer circle to inner circle.

from graphics import *

def main():
    win = GraphWin("Archery", 600, 600)
    

    #Circle 4 - White
    circle4 = Circle(Point(300, 300), 120)
    circle4.setFill("white")
    circle4.draw(win)
    update(30)
    time.sleep(2)

    #Circle 3 - Blue
    circle3 = Circle(Point(300, 300), 90)
    circle3.setFill("blue")
    circle3.draw(win)
    update(30)
    time.sleep(2)

    #Circle 2 - Red
    circle2 = Circle(Point(300, 300), 60)
    circle2.setFill("red")
    circle2.draw(win)
    update(30)
    time.sleep(2)

    #Circle 1 - Yellow
    circle1 = Circle(Point(300, 300), 30)
    circle1.setFill("yellow")
    circle1.draw(win)
    update(30)
    time.sleep(0.1)

    input()
    win.close()


main()
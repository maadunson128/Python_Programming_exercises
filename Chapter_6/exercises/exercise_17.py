###Program: Moving Circle

#importing libraries
from graphics import *

#function to move the circle
def moveTo(shape, newCenter):
    old_center = shape.getCenter()
    #calculating the distances to be moved in x and y directions
    dx = newCenter.getX() - old_center.getX()
    dy = newCenter.getY() - old_center.getY()
    shape.move(dx, dy)
    

def main()->None:

    win = GraphWin('Circle moving', 600, 600)

    #drawing circle at Point(300, 300)
    circle = Circle(Point(300, 300), 20)
    circle.setFill('blue')
    circle.draw(win)

    for i in range(10):
        #getting the new center for the object to be moved
        newCenter = win.getMouse()
        moveTo(circle, newCenter)

    
main()
    

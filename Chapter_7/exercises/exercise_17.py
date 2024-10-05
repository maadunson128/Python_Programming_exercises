###Program: Bouncing circle
from graphics import *

#function to draw a circle moving
def bouncing_circle(win)->None:
    circle = Circle(Point(100, 200), 20)
    circle.draw(win)

    #initial dx and dy values
    dx = 1
    dy = 1
    
    #making the circle to bounce when it reaches boundary
    for i in range(10000):
        x = circle.getCenter().getX()
        y = circle.getCenter().getY()
        
        #changing dx and dy if hits boundary
        if x <= 0 or x>= 700:
            dx -= 1
        if y<= 0 or y>= 600:
            dy -= 1
        
        circle.move(dx, dy)
        update(30)
        
        



def main()->None:
    #window creation
    win = GraphWin("Bouncing circle", 700, 600)

    #Making the circle to move and bounce when hit on boundary
    bouncing_circle(win)    


main()

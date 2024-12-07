###Program: Three door monte
from random import randint
from graphics import *


class Button:
    def __init__(self, win, center, width, height, label):
        '''Creates an instance of button and draws a rectangle with label text inside it.
        '''
        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmin, self.xmax = x-w, x+w
        self.ymin, self.ymax = y-h, y+h
        pt1 = Point(self.xmin,  self.ymin)
        pt2 = Point( self.xmax,  self.ymax)
        
        rect = Rectangle(pt1, pt2)
        rect.setFill('lightgrey')
        rect.draw(win)

        text = Text(center, label)
        text.draw(win)

    def clicked(self, pt):
        if (self.xmin <= pt.getX() <= self.xmax and
                self.ymin <= pt.getY() <= self.ymax):
            return True

def main()->None:

    #Random door as a special door
    win_door = randint(1,3)

    #window creation
    win = GraphWin("Three door monte", 1000, 600)
    
    #creating three buttons
    button1 = Button(win, Point(250, 250), 100, 50, "Door 1")
    button2 = Button(win, Point(500, 250), 100, 50, "Door 2")
    button3 = Button(win, Point(750, 250), 100, 50, "Door 3")

    
    #checking which button is clicked
    text1 = Text(Point(500, 100), "Click on any door")
    text1.draw(win)

    pt = win.getMouse()
    clicked_button = 0
    if button1.clicked(pt):
        clicked_button = 1
    elif button2.clicked(pt):
        clicked_button = 2
    elif button3.clicked(pt):
        clicked_button = 3


    # Printing the results
    if clicked_button == win_door:
        Text(Point(500, 400), "You won").draw(win)
    else:
        Text(Point(500, 400), f"You lose.\nThe correct door: {win_door}").draw(win)
        


main()

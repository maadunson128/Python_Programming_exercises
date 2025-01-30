###Program: Creating Die Game using Lists and Objects
from graphics import *
from random import randrange

class DieView:
    """This class creates a Die with circle pips inside it."""

    def __init__(self, win, center, size):
        self.win = win
        self.background = 'white'
        self.foreground = 'black'

        hsize = size/2.0
        self.psize = size * 0.1
        offset = hsize * 0.6 
        cx, cy = center.getX(), center.getY()

        pt1 = Point(cx-hsize, cy+hsize)
        pt2 = Point(cx+hsize, cy-hsize)

        rect = Rectangle(pt1, pt2)
        rect.setFill(self.background)
        rect.draw(win)

        #creating the pips (circles)
        self.pips = [self.__makepip(cx-offset, cy-offset),
                     self.__makepip(cx-offset, cy),
                     self.__makepip(cx-offset, cy+offset),
                     self.__makepip(cx, cy),
                     self.__makepip(cx+offset, cy-offset),
                     self.__makepip(cx+offset, cy),
                     self.__makepip(cx+offset, cy+offset)
                     ]
        #list for circles to be on
        self.onTable = [[],
                   [3],
                   [2, 4],
                   [2, 3, 4],
                   [0, 2, 4, 6],
                   [0, 2, 3, 4, 6],
                   [0, 1, 2, 4, 5, 6]
                   ]
        
        self.setValue(5)

    def __makepip(self, x, y):
        """Draws the circle and return the pip object"""
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        
        return pip
    
    def setValue(self, value):
        '''Sets the respective pips to turn on for the value'''
        self.value = value
        #turn off all the pips
        for pip in self.pips:
            pip.setFill(self.background)

        #turn on thr respective pips
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)

    def setColor(self, color):
        self.foreground = color
        self.setValue(self.value)


class Button:
    def __init__(self, win, center, width, height, text):
        self.win = win

        #drawing the button
        cx, cy = center.getX(), center.getY()
        w = width/2.0
        h = height/2.0
        self.xmin, self.ymin = cx-w, cy-h
        self.xmax, self.ymax = cx+w, cy+h
        pt1 = Point(self.xmax, self.ymax)
        pt2 = Point(self.xmin, self.ymin)
        self.rect = Rectangle(pt1, pt2)
        self.rect.setOutline("black")
        self.rect.draw(win)
        

        #label inside the rectangle
        self.label = Text(center, text)
        self.label.draw(win)

        self.deactivate()

    def clicked(self, pt):
        '''Return True if button is clicked'''
        
        return (self.active and
                self.xmin <= pt.getX() <= self.xmax and
                self.ymin <= pt.getY() <= self.ymax)

    def activate(self):
        '''Activates the button'''
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        '''Deactivates the button'''
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def getLabel(self):
        '''Returns the label of the button'''
        return self.label.getText()


def main():

    win = GraphWin("Die game", 700, 500)
    win.setCoords(0, 0, 10, 10)
    die1 = DieView(win, Point(3, 7), 3)
    die2 = DieView(win, Point(7, 7), 3)

    b1 = Button(win, Point(5, 4), 1, 1, "Quit")
    b2 = Button(win, Point(5, 1), 1, 1, "Roll")
    b2.activate()
    
    pt = win.getMouse()
    # entire button and dice functionalities
    while not b1.clicked(pt):
        
        if b2.clicked(pt):
            #die 1 functionality
            value1 = randrange(1, 7)
            die1.setValue(value1)
            b1.activate()

            #die 2 functionality
            value2 = randrange(1, 7)
            die2.setValue(value2)
            b2.activate()

        pt = win.getMouse()

    win.close()

if __name__ == "__main__":
    main()


###Program: Regression line using class
from graphics import *
import math

class Regression:
    """Creates an window that can draw regression line for points clicked"""

    def __init__(self, win):
        """Creates a window with Quit button for regression line"""
        self.win = win
        self.points = []
        
        ##drawing the done box
        rect = Rectangle(Point(30, 30), Point(120, 65))
        rect.draw(win)

        #drawing the text inside the box
        text = Text(rect.getCenter(), "DONE")
        text.draw(win)

    def drawPoint(self, pt):
        """Drwas the point in the window"""
        circle = Circle(pt, 3)
        circle.setFill("black")
        circle.draw(self.win)
        

    def addPoint(self, pt):
        """Adds the point for regression line calculation"""
        self.points.append(pt)

    def predict(self, xpos):
        """Returns the predicted y-position for the given x-position"""
        ypos = self.mean_y + self.m * (xpos - self.mean_x)
        return ypos
        
    def drawLine(self):
        """Draws the regression line"""
        count = len(self.points)
        self.mean_x, self.mean_y, sum_x2, sum_xy = self.find_params(self.points, count)
        self.m = (sum_xy - count * (self.mean_x) * self.mean_y) / (sum_x2 - count * (self.mean_x**2))

        #Two points to draw the regression line  
        pt_x1 = 0
        pt_x2 = 1000
        pt_y1 = self.mean_y + self.m * (pt_x1 - self.mean_x)
        pt_y2 = self.mean_y + self.m * (pt_x2 - self.mean_x)

        #drawing the regression line
        line = Line(Point(pt_x1, pt_y1), Point(pt_x2, pt_y2))
        line.draw(self.win)

    def find_params(self, points, count):
        """Retuens the mean of x and y co-ordinates of the points clicked"""
        sum_x = 0
        sum_y = 0
        sum_x2 =0
        sum_xy = 0

        for pt in points:
            sum_x += pt.getX()
            sum_y += pt.getY()
            sum_x2 += (pt.getX() **2)
            sum_xy += pt.getX() * pt.getY()

        return sum_x/count, sum_y/count, sum_x2, sum_xy
    
    def clickedQuit(self, pt):
        return int(pt.getX()) in range(30, 121) and  int(pt.getY()) in range(30, 65)
        

def main()->None:

    #creating window for regression line
    win = GraphWin("Regression line window", 1000, 600)
    win.setCoords(0, 0, 1000, 600)

    reg = Regression(win)

    while True:
        pt = win.getMouse()

        if reg.clickedQuit(pt):
            break
        
        reg.drawPoint(pt)
        reg.addPoint(pt)

    reg.drawLine()

    input()
    win.close()


main()
    









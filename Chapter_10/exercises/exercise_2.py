###Program: Button class for Chapter 8 exercise 13: Regression line
from graphics import *

class Button:
    '''It creates an instance of a button in the graphical window.
    '''

    def __init__(self, win, center, width, height, label):
        self.win = win

        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmin, self.xmax, self.ymin, self.ymax = x-w, x+w, y-h, h+y
        pt1 = Point(self.xmin, self.ymin)
        pt2 = Point(self.xmax, self.ymax)
        
        self.rect = Rectangle(pt1, pt2)
        self.rect.setFill('lightgrey')
        self.rect.draw(win)

        self.label = Text(center, label)
        self.label.draw(win)

        self.activate()

    def clicked(self, pt):
        '''It return 'True' if button is clicked.
        '''
        return (self.active and
                self.xmin <= pt.getX() <= self.xmax and
                self.ymin <= pt.getY() <= self.ymax)

     
    def activate(self):
        '''Set this button to active.'''
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        '''Set this button to deactive.'''
        self.label.setFill('lightgrey')
        self.rect.setWidth(1)
        self.active = False

    def getLabel(self):
        '''Returns the label from the button.'''
        return self.label.getText()

class Regression:
    '''This will create a Regression window.'''

    def __init__(self, win):
        self.win = win
        self.initial_values()

    def initial_values(self):
        self.circles = []
        self.count = 0
        self.sum_x = 0
        self.sum_y = 0
        self.sum_x2 = 0
        self.sum_xy = 0
        self.mean_x = 0
        self.mean_y = 0
        self_m = 0
        self.pt_y1 = 0
        self.pt_y2 = 0
        self.pt_x1 = 0
        self.pt_x2 = 1000
        self.lineIsdrawn = False
        self.pts_clt = False

    def update(self, pt):
        '''Draws the circle and calculates the updates the attributes for the regression line'''
        #Drawing the point and adding them into a list         
        circle = Circle(pt, 3)
        circle.setFill("black")
        circle.draw(self.win)
        self.circles.append(circle)

        x, y = pt.getX(), pt.getY()
        #running sum of x, y, x^2, xy
        self.count += 1
        self.sum_x += x
        self.sum_y += y
        self.sum_x2 += (x**2)
        self.sum_xy += (x * y)

        self.pts_clt = True

    def draw_line(self):
        '''Draws the regression line in the graphical window'''
        if self.pts_clt:
            #mean values of x, y
            self.mean_x = self.sum_x / self.count
            self.mean_y = self.sum_y/ self.count
            self.m = (self.sum_xy - self.count * (self.mean_x) * self.mean_y) / (self.sum_x2 - self.count * (self.mean_x**2))

            #Two points to draw the regression line  
        
            self.pt_y1 = self.mean_y + self.m * (self.pt_x1 - self.mean_x)
            self.pt_y2 = self.mean_y + self.m * (self.pt_x2 - self.mean_x)

            #drawing the regression line
            self.line = Line(Point(self.pt_x1, self.pt_y1), Point(self.pt_x2, self.pt_y2))
            self.line.draw(self.win)
            self.lineIsdrawn = True


    def clear(self):
        '''This will clear all the content in Graphical window'''
        for circle in self.circles:
            circle.undraw()
        if self.lineIsdrawn:
            self.line.undraw()
        self.initial_values()

    
    
    
def main():
    win = GraphWin('Regression line', 1000, 600)
    b1 = Button(win, Point(100, 550), 50, 30, 'DONE')
    b2 = Button(win, Point(500, 550), 60, 30, 'CLEAR')
    b3 = Button(win, Point(900, 550), 60, 30, 'CLOSE')
    regression = Regression(win)

    while True:
        pt = win.getMouse()

        if b1.clicked(pt):
            regression.draw_line()
        elif b2.clicked(pt):
            regression.clear()
        elif b3.clicked(pt):
            win.close()
        else:
            regression.update(pt)
            

main()
        
        

###Program: Three door monte game
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



def game()->None:


    #Random door as a special door
    win_door = randint(1,3)

    #window creation
    win = GraphWin("Three door monte", 1000, 600)
    
    #creating three buttons
    button1 = Button(win, Point(250, 250), 100, 50, "Door 1")
    button2 = Button(win, Point(500, 250), 100, 50, "Door 2")
    button3 = Button(win, Point(750, 250), 100, 50, "Door 3")
    quitButton = Button(win, Point(500, 550), 100, 50, "Quit")
    
    #checking which button is clicked
    text1 = Text(Point(500, 100), "Click on any button. You can press any door again for the next game.")
    text1.draw(win)

    wins = 0
    loses = 0
    while True:
        pt = win.getMouse()
        clicked_button = 0

        if quitButton.clicked(pt):
            break
        elif button1.clicked(pt):
            clicked_button = 1
        elif button2.clicked(pt):
            clicked_button = 2
        elif button3.clicked(pt):
            clicked_button = 3

        #counting wins, loses
        
        if clicked_button == win_door:
            wins += 1
        else:
            loses += 1

    Text(Point(500, 400), f"Total games won: {wins}\nTotal games lost: {loses}").draw(win)
    win.getMouse()

    win.close()
    
def main()->None:

    #Creating the game
    game()



        

main()

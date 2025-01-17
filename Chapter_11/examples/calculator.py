###Program: Calculator 

from list_objects import Button
from graphics import *

class Calculator:
    def __init__(self):
        '''Creates a interface for the calculator'''

        #create window for the calculator
        win = GraphWin('Calculator')
        win.setCoords(0, 0, 6, 7)
        win.setBackground('slategrey')
        self.win = win

        #creating buttons and display
        self.__createButtons()
        self.__createDisplay()

    def __createButtons(self):
        #create buttons
        bspecs = [(2 , 1 , '0'), (3 , 1 , '.' ), 
                  ( 1 ,2, '1'), (2 ,2, '2'), (3 ,2, '3' ), (4 ,2, '+' ), (5 ,2, '-' ), 
                  ( 1 ,3, '4' ), (2 ,3, '5' ), (3 ,3, '6'), (4 ,3, '*'), (5 ,3, '/' ), 
                  (1,4, '7' ), (2 ,4, '8' ), (3 ,4, '9'), (4 ,4, '<-' ), (5,4, 'C' )]
        self.buttons = []

        for (cx, cy, label) in bspecs:
            self.buttons.append(Button(self.win, Point(cx, cy), .75, .75, label))

        #creating the '=' button
        self.buttons.append(Button(self.win, Point(4.5, 1), .75, 1.75, '='))

        #activate all buttons
        for button in self.buttons:
            button.activate()

    def __createDisplay(self):
        #creating the display
        bg = Rectangle(Point(.5, 5.5), Point(5.5, 6.5))
        bg.setFill('white')
        bg.draw(self.win)
        text = Text(Point(3, 6), "")
        text.draw(self.win)
        text.setFace('courier')
        text.setStyle('bold')
        text.setSize(16)
        self.display = text

    def getKeyPress(self):
        '''Gets the pressed key'''
        while True:
            pt = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(pt):
                    return b.getLabel()
                    
    def processKey(self, key):
        '''Process the key'''
        text = self.display.getText()
        
        #Different operations according to the key pressed
        if key == 'C':
            self.display.setText("")
        elif key == '<-':
            self.display.setText(text[:-1])
        elif key == '=':
            try:
                result = eval(text)
            except:
                result = 'Error'
            self.display.setText(str(result))
        else:
            self.display.setText(text + key)

    def run(self):
        '''Makes the calculator to operate'''
        while True:
            key = self.getKeyPress()
            self.processKey(key)   


#Runs the entire calculator program
if __name__ == "__main__":
    #creating the calculator object  
    cal = Calculator()
    #calling the run method in it.
    cal.run()
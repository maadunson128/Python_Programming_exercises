###Program: Drawing grim face

#importing libraries
from graphics import *

#function to draw the face(grim face)
def drawFace(center, size, win)->None:
    
    x = center.getX()
    y = center.getY()
    #drawing face
    outline = Circle(center, size)
    outline.setFill("yellow")
    outline.draw(win)
    
    #drawing eyes
    #left eye
    left_eye = Circle(Point(x-(size*0.5), (y-size*0.5)), size/10)
    left_eye.setFill("brown")
    left_eye.draw(win)
    

    #right eye
    right_eye = Circle(Point(x+(size*0.5), (y-size*0.5)), size/10)
    right_eye.setFill("brown")
    right_eye.draw(win)

    #Drawing mouth as two parts
    mouth_1 = Rectangle(Point(x-(size*0.5), y+(size*0.5)),Point(x+(size*0.5), y+(size*0.55)))
    mouth_1.setFill('black')
    mouth_1.setOutline('white')
    mouth_1.draw(win) #top part 
    mouth_2 = Rectangle(Point(x-(size*0.5), y+(size*0.55)),Point(x+(size*0.5), y+(size*0.6)))
    mouth_2.setFill('black')
    mouth_2.setOutline('white')
    mouth_2.draw(win) #bottom part


def main()->None:

    #size input from the user
    size = float(input("Enter the size of the face: (50-200): "))

    #window and default center point
    win = GraphWin('Grim Face', 600, 500)
    center = Point(300, 250)

    #drawing the face
    drawFace(center, size, win)


if __name__ == "__main__":
    main()

'''The main function is commented since this file can be used as a module.'''

###Program: Photo anonymiser

#importing modules
from graphics import *
from exercise_15 import drawFace
import math

def distance(p1, p2):
    return math.sqrt(((p2.getX()-p1.getX()) **2) + ((p2.getY()-p1.getY()) **2))

    
#function to anonymise the faces
def photoAnonymiser(count:int, win)->None:

    for i in range(count):
        center = win.getMouse() # getting center of image
        edge = win.getMouse() # getting the edge for radius finding (for size calculation)
        size = distance(center, edge) #finding the distance between two points for size (radius)
        drawFace(center, size, win) #Anonymising each faces with grim emoji

    

def main()->None:

    win = GraphWin('Image Anonymiser', 640, 426)

    #image drawing on the window
    Image(Point(320, 213), 'image_2.gif').draw(win)

    #user input for count for photo faces to be anonymised
    count:int = int(input("Enter the faces to be anonymised: "))

    #Anonymising the faces on the image based on count with  grim emoji
    photoAnonymiser(count, win)


    input("")
    win.close()


main()
    
    

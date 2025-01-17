#Program: To draw a histogram based on count on marks

#importing graphics module functions
from graphics import *

def main()->None:

    #taking the input from the file
    infile = open('ex_16_data.txt', 'r')

    #array for storing the frequency of marks
    ar:list[int] = [0 for i in range(11)]

    #getting the each number in file and storing accordingly
    for line in infile:
        index = int(line.strip())
        ar[index] += 1

    print(ar)

    #Graphical window object creation
    win = GraphWin('Histogram', 1000, 600)
    win.setCoords(0,0, 1000, 600)

    #drawing the histogram
    #points for the x axis numbers
    x:int = 125
    y:int = 50
    
    #Points for the vertical rectangles
    x1:int = 100
    x2:int = 150
    y1:int = 100
    
    for i in range(11):
        #Drawing the x axis numbers
        Text(Point(x,y), str(i)).draw(win)
        
        #calculating the height and drawing the histogram
        y2:int = (ar[i] * 10) + 100
        Rectangle(Point(x1, y1), Point(x2, y2)).draw(win)
        
        #updating the values for next values
        x1 +=75
        x2 +=75
        x+=75


main()
        

#Program: Drawing Archery target board with points calculation

#importing modules
from graphics import *
import math

#function to draw the archery board
def draw_board(win)->None:

   
    color = ['white', 'black', 'blue', 'red', 'yellow']
    radius = [150, 120, 90, 60, 30]
    circle = []
    #drawing the 4 circles
    for i in range(5):
        circle.append(Circle(Point(300, 300), radius[i]))
        circle[i].setFill(color[i])
        circle[i].draw(win)


#function to find the scores
def calculate_score(pts)->int:

    score:int = 0
    #Calculating score for each points
    for pt in pts:
        #distance of point from center and giving score according to the circle colors
    
        distance = math.sqrt(((pt.getX() - 300) **2) + ((pt.getY() - 300) **2))
        print(distance)
        if distance <= 30:
            score += 9 #yellow
        elif distance <= 60:
            score += 7 #red
        elif distance <= 90:
            score += 5 #blue
        elif distance <= 120:
            score += 3 #black
        elif distance <= 150:
            score += 1 #white
        else:
            score += 0 #outside the archery board

    return score
            
    
    
def main()->None:

    win = GraphWin("Archer board", 600, 600)
    #drawing the archery board
    draw_board(win)

    #getting the five points clicked on the archery board
    pts = []
    for i in range(5):
        pts.append(win.getMouse())

    #Finding the score
    score = calculate_score(pts)

    Text(Point(300, 500), f"Score: {score} points").draw(win)
    


main()

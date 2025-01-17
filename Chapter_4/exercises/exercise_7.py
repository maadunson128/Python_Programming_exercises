###Program: To draw a circle with its intersection with y-intercept

from graphics import *
import math

def main():
    
    print("Note: Please enter a radius less than 9.")

    #Getting the input values
    radius = float(input("Enter the radius: "))
    y_intercept = float(input("Enter the y-intercept of the line: "))

    if radius <= 9:
        if radius >= y_intercept:

            win = GraphWin('Circle Intersection', 600, 600)
            win.setCoords(-10, -10, 10, 10)

            #Intersection points calculation
            x1 = math.sqrt((radius ** 2) - (y_intercept **2))
            x2 = -abs(math.sqrt((radius ** 2) - (y_intercept **2)))
            
            #Drawing the circle and the line
            cir = Circle(Point(0,0), radius)
            cir.draw(win)

            line = Line(Point(-10, y_intercept), Point(10, y_intercept))
            line.draw(win)

            #Drawing the intersection points
            p1 = Point(x1, y_intercept)
            p1.setFill("red")
            p1.draw(win)

            p2 = Point(x2, y_intercept)
            p2.setFill("red")
            p2.draw(win)


            Text(Point(-1, -7), f'Intersection x points : x1 = {x1}, x2 = {x2}').draw(win)




            input()
            win.close()

        else:
            print("The y-intercept is larger than radius. The circle wont interesect with the line.")

    else:
        print("The radius is less than 9")

main()
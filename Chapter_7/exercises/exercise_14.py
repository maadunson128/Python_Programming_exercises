'''Circle Intersection.
Write a program that computes the intersection of a circle with a horizontal
line and displays the information textually and graphically.
Input: Radius of the circle and they-intercept of the line.
Output: Draw a circle centered at (0, 0) with the given radius in a window
with coordinates running from -10,-10 to 10, 10.
Draw a horizontal line across the window with the given y-intercept.
Draw the two points of intersection in red.
Print out the x values of the points of intersection.
Formula: x = ±y'r2 - y2'''


###Program: Drawing the intersection points with cases
from graphics import *
from math import sqrt


#function for findind and drawing the intersection points
def find_intersection(radius:float, y_intercept:float)->None:

    #Window for graphical interface
    win = GraphWin("Circle Intersection point", 600, 600)
    win.setCoords(-10, -10, 10, 10)

    #drawing the circle
    circle = Circle(Point(0, 0), radius)
    circle.draw(win)

    #drawing the y-intercept line
    y_inter_line = Line(Point(-10, y_intercept), Point(10, y_intercept))
    y_inter_line.draw(win)

    #Text box for showing Intersection points
    text = Text(Point(0, -7), "")
    text.draw(win)

    
    #Drawing the intersections points of there any
    if radius >= y_intercept:
        #finding two x values of points
        x1:float = sqrt((radius ** 2) - (y_intercept ** 2))
        x2:float = -1 * x1

        pt1 = Point(x1, y_intercept)
        pt1.setFill("red")
        pt1.draw(win)
        
        pt2 = Point(x2, y_intercept)
        pt2.setFill("red")
        pt2.draw(win)

        text.setText(f"Intersection Points: \n({x1}, {y_intercept}) ({x2}, {y_intercept})")
        
    #handling case where 
    else:
        text.setText(f"There is no intersection points for circle with \n radius {radius} and horizontal line with y-intercept {y_intercept}")
        





def main()->None:
    #user input: radius and y-intercept
    print(f"Please enter radius and y-intercept within the below ranges: \n1.Radius: 0 to 10 \nY-intercept: -10 to 10")
    radius:float = float(input("Enter the radius: "))
    y_intercept = float(input("Enter the y-intercept: "))

    #finding the intersection points with handling non-intersection points
    find_intersection(radius, y_intercept)



main()

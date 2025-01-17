###Program: Regression line draw

from graphics import *

#function for drawing the regression line
def draw_line(win)->None:

    ##drawing the done box
    rect = Rectangle(Point(30, 30), Point(120, 65))
    rect.draw(win)

    #drawing the text inside the box
    text = Text(rect.getCenter(), "DONE")
    text.draw(win)


    count:int = 0
    sum_x:int = 0
    sum_y:int = 0
    sum_x2:int = 0
    sum_xy:int = 0
    while True:
        clt_pt = win.getMouse()

        x = clt_pt.getX()
        y = clt_pt.getY()
        print(x, y)
        
        #condition for exiting the loop(when clicked on Done text)
        if int(x) in range(30, 121) and int(y) in range(30, 65):
            break

        #Drawing the point and adding them into a list
        circles = []
        circle = Circle(clt_pt, 3)
        circle.setFill("black")
        circle.draw(win)
        circles.append(circle)
        
        #running sum of x, y, x^2, xy
        count += 1
        sum_x += x
        sum_y += y
        sum_x2 += (x**2)
        sum_xy += (x * y)

    ##calculation of slope m
    #mean values of x, y
    mean_x = sum_x / count
    mean_y = sum_y/ count
    m = (sum_xy - count * (mean_x) * mean_y) / (sum_x2 - count * (mean_x**2))

    #Two points to draw the regression line  
    pt_x1 = 0
    pt_x2 = 1000
    pt_y1 = mean_y + m * (pt_x1 - mean_x)
    pt_y2 = mean_y + m * (pt_x2 - mean_x)

    #drawing the regression line
    line = Line(Point(pt_x1, pt_y1), Point(pt_x2, pt_y2))
    line.draw(win)
        

    
def main()->None:

    #window for drawing the regression line
    win = GraphWin("Regression line", 1000, 600)
    win.setCoords(0, 0, 1000, 600)

    #draw the regression line
    draw_line(win)


main()

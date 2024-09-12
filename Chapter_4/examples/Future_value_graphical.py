###Program: Graphical interface for Future value program in chapter 2

from graphics import *
def main():
    #Introduction
    print("Graphical interface for Future value Program")

    #Taking the inputs -> Principal amount, apr (annual percentage rate)
    principal = float(input("Enter the principal amount: "))
    apr = float(input("Enter the annual interest rate: "))

    #Drawing the label in Graphical window
    win = GraphWin("Interest Grow chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), ' 0.0k').draw(win)
    Text(Point(20, 180), ' 2.5k').draw(win)
    Text(Point(20, 130), ' 5.0k').draw(win)
    Text(Point(20, 80), ' 7.5k').draw(win)
    Text(Point(20, 30), '10.0k').draw(win)

    #Drawing bar chart for initial pricipal amount
    height = principal * 0.02
    rect = Rectangle(Point(40, 230), Point(65, 230 - height))
    rect.setFill("yellow")
    rect.setWidth(2)
    rect.draw(win)

    #Drawing the bar chart for principal amounts from year 1 to year 10
    for year in range(1,11):
        principal = principal * (1 + apr / 100)
        #Left edge point
        xaxis1 = (25 * year + 40)
        height = principal * 0.02
        bar = Rectangle(Point(xaxis1, 230), Point(xaxis1 + 25, 230 - height))
        bar.setFill("yellow")
        bar.setWidth(2)
        bar.draw(win)

    input("Press Enter key")
    win.close()


main()

    

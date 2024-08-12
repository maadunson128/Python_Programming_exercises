###Program:  modified version of future value


from graphics import *
def main():
    #Introduction
    print("Graphical interface for Future value Program")

    
    #Drawing the label in Graphical window
    win1 = GraphWin("Interest Grow chart", 320, 240)
    win1.setBackground("white")

    #Geting the principal amount and interest

    prin = Text(Point(65, 50), 'Principal amount: ')
    int_text = Text(Point(55, 75), 'Interest rate:')
    prin.draw(win1)
    int_text.draw(win1)
    princ = Entry(Point(180, 50), 10)
    interest = Entry(Point(160, 75), 8)
    princ.setText('0.0')
    princ.draw(win1)
    interest.setText('0')
    interest.draw(win1)
    

    a = Text(Point(150, 160), 'Visualise Future Value').draw(win1)
    b = Rectangle(Point(50, 150), Point(280, 180)).draw(win1)
    point = win1.getMouse()
    principal = float(princ.getText())
    apr = float(interest.getText())

    prin.undraw()
    int_text.undraw()
    interest.undraw()
    princ.undraw()
    a.undraw()
    b.undraw()
    
    x = point.getX()
    y = point.getY()

    print(principal, apr)

    

    if (x in range(320)) and (y in range(240)):
    
        
        Text(Point(20, 230), ' 0.0k').draw(win1)
        Text(Point(20, 180), ' 2.5k').draw(win1)
        Text(Point(20, 130), ' 5.0k').draw(win1)
        Text(Point(20, 80), ' 7.5k').draw(win1)
        Text(Point(20, 30), '10.0k').draw(win1)

        #Drawing bar chart for initial pricipal amount
        height = principal * 0.02
        rect = Rectangle(Point(40, 230), Point(65, 230 - height))
        rect.setFill("yellow")
        rect.setWidth(2)
        rect.draw(win1)
        

        #Drawing the bar chart for principal amounts from year 1 to year 10
        for year in range(1,11):
            principal = principal * (1 + apr / 100)
            #Left edge point
            xaxis1 = (25 * year + 40)
            height = principal * 0.02
            bar = Rectangle(Point(xaxis1, 230), Point(xaxis1 + 25, 230 - height))
            bar.setFill("yellow")
            bar.setWidth(2)
            bar.draw(win1)

        input("Press Enter key")
        win1.close()


main()

    

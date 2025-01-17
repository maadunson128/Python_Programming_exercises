###Program: Drawing 5 dices

from graphics import *

def main():
    win = GraphWin('5 Dices', 1200, 600)

    #Drawing 5 dices
    dice1 = Rectangle(Point(33, 200), Point(233, 400))
    dice1.draw(win)

    dice2 = Rectangle(Point(266, 200), Point(466, 400))
    dice2.draw(win)

    dice3 = Rectangle(Point(499, 200), Point(699, 400))
    dice3.draw(win)

    dice4 = Rectangle(Point(732, 200), Point(932, 400))
    dice4.draw(win)

    dice5 = Rectangle(Point(965, 200), Point(1165, 400))
    dice5.draw(win)

    #Drawing circles inside dice 5
    dice511 = Circle(Point(1009, 231), 12.5)
    dice511.draw(win) 

    dice512 = Circle(Point(1121, 231), 12.5)
    dice512.draw(win)

    dice521 = Circle(Point(1009, 300), 12.5)
    dice521.draw(win)

    dice522 = Circle(Point(1121, 300), 12.5)
    dice522.draw(win)

    dice531 = Circle(Point(1009, 369), 12.5)
    dice531.draw(win)


    dice532 = Circle(Point(1121, 369), 12.5)
    dice532.draw(win)
    

    #Dice 4 inside circles drawing
    dice411 = Circle(Point(775.5, 231), 12.5)
    dice411.draw(win)

    dice412 = Circle(Point(888.5, 231), 12.5)
    dice412.draw(win)

    dice42 = Circle(Point(832, 300), 12.5)
    dice42.draw(win)

    dice431 = Circle(Point(775.5, 369), 12.5)
    dice431.draw(win)

    dice432 = Circle(Point(888.5, 369), 12.5)
    dice432.draw(win)

    #Dice 3 inside drawing

    dice311 = Circle(Point(542.5, 231), 12.5)
    dice311.draw(win)

    dice312 = Circle(Point(655.5, 231), 12.5)
    dice312.draw(win)

    dice321 = Circle(Point(542.5, 369), 12.5)
    dice321.draw(win)
    
    dice322 = Circle(Point(655.5, 369), 12.5)
    dice322.draw(win)

    #Dice 2 inside circles drawing

    dice211 = Circle(Point(423, 231), 12.5)
    dice211.draw(win)

    dice221 = Circle(Point(366, 300), 12.5)
    dice221.draw(win)

    dice231 = Circle(Point(309.5, 369), 12.5)
    dice231.draw(win)

    #Dice 1 drawing

    dice11 = Circle(Point(76.5, 231), 12.5)
    dice11.draw(win)

    dice12 = Circle(Point(189.5, 369), 12.5)
    dice12.draw(win)

    input("")
    win.close()

main()
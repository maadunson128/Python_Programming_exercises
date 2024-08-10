#Program: Draw a face

from graphics import *
def main():
    win = GraphWin("Face", 500, 500)
    #Outer face surrounding
    oval = Oval(Point(125, 50), Point(375, 450))
    oval.draw(win)

    #Eyes
    left_eye = Circle(Point(190, 180), 10)
    left_eye.draw(win)

    right_eye = Circle(Point(300, 180), 10)
    right_eye.draw(win)

    #Drawing nose
    nose = Rectangle(Point(248, 240), Point(255, 247))
    nose.draw(win)

    #Drawing mouth
    mouth = Rectangle(Point(185, 320), Point(330,300 ))
    mouth.draw(win)


    input("")

main()
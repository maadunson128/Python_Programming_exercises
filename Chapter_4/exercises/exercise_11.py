###Program: Drawing a house

from graphics import *

def main():
    win = GraphWin('House', 700, 700)
    pt1 = win.getMouse()
    pt2 = win.getMouse()

    Rectangle(pt1, pt2).draw(win)

    pt3 = win.getMouse()
    #Door
    width = abs(pt1.getX() - pt2.getX())
    door_width = width / 5

    door_x1 = pt3.getX() - door_width / 2
    door_y1 = pt3.getY()

    door_x2 = pt3.getX() + door_width /2
    door_y2 = pt1.getY()

    Rectangle(Point(door_x1, door_y1), Point(door_x2, door_y2)).draw(win)

    #window
    pt4 = win.getMouse()
    window_width = door_width / 2
    window_x1 = pt4.getX() - window_width /2
    window_y1 = pt4.getY() - window_width /2
    window_x2 = pt4.getX() + window_width /2
    window_y2 = pt4.getY() + window_width /2

    Rectangle(Point(window_x1, window_y1), Point(window_x2, window_y2)).draw(win)


    #Triangle
    pt5 = win.getMouse()
    pt_temp = Point(pt1.getX(), pt2.getY())

    Polygon(pt5, pt2, pt_temp).draw(win)



    input()
    win.close()

main()
###Program: Drawing a triangle in Graphical Window


from graphics import *
def triangle_draw():
    #creating a object for graphical windows
    win = GraphWin("Traingle Drwaing", 500, 500)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    message = Text(Point(5, 9),"Click on three points to draw a triangle")
    message.draw(win)

    #Getting the points for the trinagle
    p1 = win.getMouse()
    p1.draw(win)

    p2 = win.getMouse()
    p2.draw(win)

    p3 = win.getMouse()
    p3.draw(win)

    #Drawing the trinagle using the points
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("yellow")
    triangle.setOutline("cyan")
    triangle.draw(win)

    message.setText("Click any point to exit.")
    win.getMouse()
    win.close()


triangle_draw()

    
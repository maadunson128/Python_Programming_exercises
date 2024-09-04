from graphics import *

def left_justified_text(win, point, text_string):
    text = Text(point, text_string)
    text.draw(win)

win = GraphWin("Left Justified Text", 400, 200)

# Example usage
left_justified_text(win, Point(50, 50), "This text is left justified")

win.getMouse()
win.close()

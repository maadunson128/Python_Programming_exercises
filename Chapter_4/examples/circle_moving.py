from graphics import *
import time

win = GraphWin("Moving Circle", 400, 300)

c = Circle(Point(10, 150), 20)
c.draw(win)

for i in range(580):
    c.move(1, 0)
    update(30)  # Limit to 30 frames per second
    time.sleep(0.01)

win.close()


'''
The for loop will be run 580 times in a fraction of second or even less
But, when we are giving the update(30), it will make the speed of changing limited to 30 frames
per second. then it is followed by 0.01 seconds delay.
'''
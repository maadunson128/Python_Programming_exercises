from graphics import *
import math
import random

class Face:
    def __init__(self, win, center, size):
        self.win = win
        self.center = center
        self.size = size
        self.face = Circle(center, size)
        self.face.setFill('yellow')
        self.face.draw(win)
        
        self.left_eye = Circle(Point(center.getX() - size / 3, center.getY() - size / 3), size / 10)
        self.left_eye.setFill('black')
        self.left_eye.draw(win)
        
        self.right_eye = Circle(Point(center.getX() + size / 3, center.getY() - size / 3), size / 10)
        self.right_eye.setFill('black')
        self.right_eye.draw(win)
        
        self.mouth = Line(Point(center.getX() - size / 2, center.getY() + size / 3),
                          Point(center.getX() + size / 2, center.getY() + size / 3))
        self.mouth.draw(win)
        
    def move(self, dx, dy):
        self.face.move(dx, dy)
        self.left_eye.move(dx, dy)
        self.right_eye.move(dx, dy)
        self.mouth.move(dx, dy)
        self.center.move(dx, dy)
        
    def smile(self, center_point, radius, start_angle, end_angle, window):
        self.mouth.undraw()
        theta = start_angle
        while theta < end_angle:
            x_coord = math.sin(theta) * radius + center_point.getX()
            y_coord = -math.cos(theta) * radius + center_point.getY()
            point1 = Point(x_coord, y_coord)
            point1.draw(window)
            theta += 0.03
            
    def frown(self, center_point, radius, start_angle, end_angle, window):
        self.mouth.undraw()
        theta = start_angle
        while theta < end_angle:
            x_coord = math.sin(theta) * radius + center_point.getX()
            y_coord = -math.cos(theta) * radius + center_point.getY()
            point1 = Point(x_coord, y_coord)
            point1.draw(window)
            theta += 0.03
            
    def wink(self, center_point, radius, start_angle, end_angle, window):
        self.mouth.undraw()
        theta = start_angle
        while theta < end_angle:
            x_coord = math.sin(theta) * radius + center_point.getX()
            y_coord = -math.cos(theta) * radius + center_point.getY()
            point1 = Point(x_coord, y_coord)
            point1.draw(window)
            theta += 0.03

def main():
    win = GraphWin("Bouncing Face", 700, 600)
    face = Face(win, Point(350, 300), 100)
    
    dx, dy = 5, 5
    expressions = [face.smile, face.frown, face.wink]
    current_expression = 0
    
    while True:
        face.move(dx, dy)
        center = face.center
        
        if center.getX() - face.size <= 0 or center.getX() + face.size >= win.getWidth():
            dx = -dx
            
        
        if center.getY() - face.size <= 0 or center.getY() + face.size >= win.getHeight():
            dy = -dy
            
        
        time.sleep(0.05)
        
    win.close()


main()
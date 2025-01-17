###program: Animated cannon ball
from graphics import *

#projectile class
class Projectile:
    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = math.radians(angle)
        self.xvel = velocity * math.cos(theta)
        self.yvel = velocity * math.sin(theta)

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.ypos - time * 9.8
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1



def getInputs():
    a = float(input("Enter the launch angle initially: "))
    v = float(input("Enter the initial velocity: "))
    h = float(input("Enter the initial height: "))
    t = float(input("Enter the time where the positions has to be updated: "))

    return a, v, h, t


#class for shot tracker
class shotTracker:
    def __init__(self, win, angle, velocity, height):
        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)

    def update(self):

        #updating the projectile class
        self.proj.update(dt)

        #updating the circle poition
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx, dy)

    def getX(self):
        return self.proj.getX()

    def getY(self):
        return self.proj.getY()

    def undraw(self);
        self.marker.undraw()

        

def main():
    #creating the animation window
    win = GraphWin("Cannon ball window", 600, 400)
    win.setCoords(-10, -10, 210, 155)

    #creating the baseline
    Line(Point(-10, 0), Point(210, 0)).draw(win)

    #creating the x-axis scale
    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)

main()
        

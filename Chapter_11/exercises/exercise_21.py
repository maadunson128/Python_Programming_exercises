###Program: Cannonball animation Updated

import math
from graphics import *
import random


class Projectile:
    """This class will take care of object that is in projection"""

    def __init__(self, angle, velocity, height):
        """It initialises x and y pos of the projectile ball"""
        theta = math.radians(angle)
        self.xpos = 0.0
        self.ypos = height
        self.xvel = velocity * math.cos(theta)
        self.yvel = velocity * math.sin(theta)

    def update(self, dt):
        """Updates the position of the ball for the given time interval"""
        self.xpos = self.xpos + self.xvel * dt
        self.yvel = self.yvel - dt * 9.8
        self.ypos = self.ypos + dt * self.yvel

    def getX(self):
        """Returns the X position of object."""
        return self.xpos
    
    def getY(self):
        """Returns the Y position of object."""
        return self.ypos
    

class shotTracker:
    """Creates a object for circle representing the cannonball with its properties.
    """
    def __init__(self, win, angle, velocity, height):
        """Creates cannon ball both in GUI and with its properties"""
        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0, 0), 3)
        self.marker.setFill('red')
        self.marker.setOutline('black')
        self.marker.draw(win)

    def update(self, dt):
        """Updates the cannon ball position with respect to time dt"""
        self.proj.update(dt)

        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()

        #moving the cannonball
        self.marker.move(dx, dy)
    
    def getCenter(self):
        '''Returns the center of the Cannonball'''
        return self.marker.getCenter()
    
    def getX(self):
        """Returns the X position of cannonball"""
        return self.proj.getX()
    
    def getY(self):
        """Returns the Y position of cannonball"""
        return self.proj.getY()
    
    def undraw(self):
        """Undraws the cannonball"""
        self.marker.undraw()
    
class Launcher:
    def __init__(self, win):
        '''Creates a Launcher with properties'''
        self.win = win
        #draws the base cannon
        self.circle = Circle(Point(0, 0.0), 3)
        self.circle.setFill('red')
        self.circle.setOutline('red')
        self.circle.draw(self.win)

        #initial parameters
        
        self.vel = 40.0
        self.angle = math.radians(45.0)
        self.height = 0.0

        #creating a dummy line and redraw it
        self.arrow = Line(Point(0, 0), Point(0,0))
        #replace it with redraw method
        self.redraw()

    def redraw(self):
        '''Redraw the arrow according to velocity and angle'''

        #first, undraw the arrow and the cannon
        self.arrow.undraw()
        self.circle.undraw()

        #redrawing the cannon with the arrow
        p2 = Point(self.vel*math.cos(self.angle), 
                   self.vel*math.sin(self.angle) + self.height)
        
        self.arrow = Line(Point(0, self.height), p2)
        self.arrow.setArrow("last")
        self.arrow.setWidth(3)
        self.arrow.draw(self.win)

        self.circle = Circle(Point(0, self.height), 3)
        self.circle.setFill('red')
        self.circle.setOutline('red')
        self.circle.draw(self.win)

    def adjAngle(self, amt):
        '''Adjust the angle of the launcher'''

        self.angle = self.angle + math.radians(amt)
        self.redraw()

    def adjVel(self, amt):
        '''Adjust the velocity of the launcher'''
        
        self.vel = self.vel + amt
        self.redraw()

    def adjHeight(self, amt):
        '''Adjusts the hright of the launcher'''
        self.height = self.height + amt
        self.redraw()

    def fire(self):
        return shotTracker(self.win, math.degrees(self.angle), self.vel, self.height)
    
class Target:
    def __init__(self, win):
        '''Creates the target'''
        self.win = win
        x = random.randint(0, 215)
        p1 = Point(x-20, 20)
        self.p2 = Point(x, 0)
        self.tar = Rectangle(p1, self.p2)
        self.tar.draw(self.win)


    def changeTarget(self):
        '''Changes the position of the target'''
        self.tar.undraw()
        x = random.randint(0, 215)
        p1 = Point(x-20, 20)
        p2 = Point(x, 0)
        self.tar = Rectangle(p1, p2)
        self.tar.draw(self.win)

    def targClicked(self, pt):
        '''Checks whether the target is hit by the cannonball'''
        print(self.tar.getP1(), self.tar.getP2())
        return (self.tar.getP1().getX() <= pt.getX() <= self.tar.getP2().getX()) and \
                (self.tar.getP2().getY() <= pt.getY() <= self.tar.getP1().getY())



class ProjectileApp:
    def __init__(self):
        '''Initiates a window for the cannonball animation'''
        self.win = GraphWin("Cannonball animation", 640, 480)
        self.win.setCoords(-10, -10, 210, 155)
        Line(Point(-10, 0), Point(210, 0)).draw(self.win)
        for x in range(0, 210, 50):
            Text(Point(x, -7), str(x)).draw(self.win)
            Line(Point(x, 0), Point(x, 2)).draw(self.win)

        #add the launcher to the window
        self.launcher = Launcher(self.win)
        print("Done 1")

        #shots tracker
        self.shots = []

        #target creation
        self.tar = Target(self.win)
        self.targetHits = 0
        self.text = Text(Point(100, 90), f"You have hit the target: {self.targetHits} times ")
        self.text.draw(self.win)

    def run(self):
        '''Runs the entire cannonball animation'''

        #main animation/event loop
        while True:
            

            self.updateShots(1/30)
            self.text.setText(f"You have hit the target: {self.targetHits} times ")

            key = self.win.checkKey()
            print(key)
            if key in ['Q', 'q']:
                break
            elif key == 'Up':
                self.launcher.adjAngle(5)
            elif key == 'Down':
                self.launcher.adjAngle(-5)
            elif key == 'Left':
                self.launcher.adjVel(-5)
            elif key == 'Right':
                self.launcher.adjVel(5)
            elif key in ['f', 'F']:
                self.shots.append(self.launcher.fire())
            elif key == 'Prior':
                self.launcher.adjHeight(5)
            elif key == 'Next':
                self.launcher.adjHeight(-5)


            update(30)

        self.win.close()

    def updateShots(self, dt):
        '''Update the shots to newer position'''

        alive = []
        for shot in self.shots:
            shot.update(dt)
            pt = shot.getCenter()

            print(pt)
            if self.tar.targClicked(pt):
                shot.undraw()
                self.tar.changeTarget()
                self.targetHits += 1
            if (-10 <= shot.getX() <= 210) and (0<= shot.getY() <= 155):
                alive.append(shot)
            else:
                shot.undraw()

        self.shots = alive



ProjectileApp().run()
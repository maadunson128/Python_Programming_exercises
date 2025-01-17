from graphics import *
import math


class Button:
    '''A button is a labeled triangle in a window.
    It is activated or deactivated by using the functions activate() and deactivate() respectively.
    The clicked(pt) method will check if the button was clicked by checking the button was active and the
    pt is inside the rectangle and return 'True'.
    '''

    def __init__(self, win, center, width, height, label):
        """Creates a rectangular button."""

        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmin, self.xmax = x-w, w+x
        self.ymin, self.ymax = y-h, h+y
        pt1 = Point(self.xmin, self.ymin)
        pt2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(pt1, pt2)
        self.rect.setFill('lightgrey')
        self.rect.draw(win)

        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
        

    def clicked(self, pt):
        """Return True if button is 'active' and pt is inside the button."""
        return (self.active and
                self.xmin <= pt.getX() <= self.xmax and
                self.ymin <= pt.getY() <= self.ymax)

    def getLabel(self):
        """Returns the text in the label."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False



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
        self.yvel = self.yvel - time * 9.8 
        self.ypos = self.ypos + time * self.yvel




class shotTracker:
    def __init__(self, win, angle, velocity, height):
        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill('red')
        self.marker.setOutline('red')
        self.marker.draw(win)

    def update(self, dt):

        self.proj.update(dt)

        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()

        self.marker.move(dx, dy)

    def getX(self):
        return self.proj.getX()
    
    def getY(self):
        return self.proj.getY()
    
    def undraw(self):
        self.marker.undraw()


class inputDialog:
    def __init__(self, angle, velocity, height):
        self.win = win = GraphWin("Dialog box", 200, 300)    
        win.setCoords(0, 4.5, 4, .5)

        
        Text(Point(1,1), "Angle").draw(win)
        self.angle = Entry(Point(3,1), 5).draw(win)
        self.angle.setText(str(angle)) 

        Text(Point(1,2), "Velocity").draw(win)
        self.vel = Entry(Point(3,2), 5).draw(win)
        self.vel.setText(str(velocity))

        Text(Point(1,3), "Height").draw(win)
        self.height = Entry(Point(3,3), 5).draw(win)
        self.height.setText(str(height))

        self.fire = Button(win, Point(1,4), 1.25, .5, "Fire ! ")
        self.fire.activate()
        self.quit = Button(win, Point(3,4), 1.25, .5, "Quit")
        self.quit.activate() 


    def interact(self):
        while True:
            pt = self.win.getMouse()

            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"
            
    def getValues(self):
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        h = float(self.height.getText())

        return a, v, h

    def close(self):
        self.win.close()


def main()->None:
    win = GraphWin("cannonball", 640, 480, autoflush=False)
    win.setCoords(-10, -10, 210, 155)

    Line(Point(-10, 0), Point(210, 0)).draw(win)

    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)

    
    angle, velocity, height = 45, 43, 2.1
    dialog = inputDialog(angle, velocity, height)
    while True:
        
        choice = dialog.interact()
        #dialog.close()
        
        if choice == "Quit":
            break

        angle, velocity, height = dialog.getValues()
        shot = shotTracker(win, angle, velocity, height)

        while -10 <= shot.getX() <= 210 and 0 <= shot.getY():
            shot.update(1/50)
            update(50)

    win.close()

main()
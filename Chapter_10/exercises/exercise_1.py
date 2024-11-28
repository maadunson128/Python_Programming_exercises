###Program: Projectile maximum height
from math import cos, sin, radians

def getInputs():
    height = float(input("Enter the initial height of the object: "))
    initial_velocity = float(input("Enter the initial velocity of the ball: "))
    angle = float(input("Enter the angle in degrees in which the ball is fired: "))
    time = float(input("Enter the time to update the positions in seconds: "))

    return height, initial_velocity, angle, time


class Projectile:
    '''This class creates a Projectile which simulates the Cannonball function.
    '''

    def __init__(self, velocity, height, angle):
        '''This function initialises the function attributes when an object of Projectile class is instantiated.
        '''
        self.ypos = self.ymax = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
        


    def update(self, time):
        '''This function updates the x-position and y-position of the object for the given time.
        '''
        self.xpos = self.xpos + time * self.xpos
        yvel1 = self.yvel - time * 9.8
        ytemp = self.ypos
        self.ypos = self.ypos + time * (yvel1 + self.yvel)/2.0
        self.ypos = yvel1

        if self.ypos >= ytemp:
            ymax = self.ypos
        else:
            ymax = ytemp


    def getX(self):
        '''This function will track the X-position of the object.'''
        return self.xpos

    def getY(self):
        '''This function will track the Y-position of the object.'''
        return self.ypos

    def getMaxY(self):
        '''This function will track the maximum height of the object.'''
        return self.ymax


def main()->None:

    #getting inputs
    in_vel, height, angle, time = getInputs()

    #creating a projectile class for cannonball
    c_ball = Projectile(in_vel, height, angle)

    #logic to get maximum height
    while c_ball.getY() <= 0.0:
        c_ball.update(time)


    print(f"The maximum height: {c_ball.getMaxY()}")

main()

###Program: Projectile class creation
import math

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
        self.yvel = self.ypos - time * 9.8
        self.ypos = self.ypos + time * self.yvel
       

def getInputs():
    a = float(input("Enter the launch angle initially: "))
    v = float(input("Enter the initial velocity: "))
    h = float(input("Enter the initial height: "))
    t = float(input("Enter the time where the positions has to be updated: "))

    return a, v, h, t

def main()->None:
    angle, velocity, height, time = getInputs()

    cball = Projectile(angle, velocity, height)

    while cball.getY() >= 0.0:
        print(cball.getY())
        cball.update(time)

    print(f"The total distance travelled by the cannon ball: {cball.getX():0.1f}")


main()        
    

    

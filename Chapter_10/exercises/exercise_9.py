
###Program: Finding area and volume of sphere
import math

class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius
    
    def surfaceArea(self):
        return 4 * math.pi * (self.radius**2)
     
    def volume(self):
        return 4/3 * math.pi * (self.radius **3)
    

def main()->None:

    #creating a sphere class
    sphere = Sphere(5)

    #surface and volume displaying
    print(f"Surface Area of sphere with radius {sphere.getRadius()}: {sphere.surfaceArea():.3f} square units.")
    print(f"Volume of sphere with radius {sphere.getRadius()}: {sphere.volume():.3f} cubic units.")


main()
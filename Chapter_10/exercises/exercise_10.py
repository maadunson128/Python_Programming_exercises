
###Program: Finding area and volume of cube

class Cube:

    def __init__(self, side):
        self.side = side

    def getSide(self):
        return self.side
    
    def surfaceArea(self):
        return 6 * (self.side**2)
     
    def volume(self):
        return self.side**3
    

def main()->None:

    #creating a sphere class
    cube = Cube(10)

    #surface and volume displaying
    print(f"Surface Area of cube with side {cube.getSide()} units: {cube.surfaceArea():.3f} square units.")
    print(f"Volume of sphere with side {cube.getSide()} units: {cube.volume():.3f} cubic units.")


main()
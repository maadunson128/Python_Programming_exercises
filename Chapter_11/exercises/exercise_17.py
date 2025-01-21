###Program: Graphics Objects as a Group

from graphics import *

class GraphicsGroup:
    def __init__(self, anchor):
        self.anchor = anchor
        self.objGroup = [anchor]


    def getAnchor(self):
        '''Returns the anchor point'''
        return self.anchor
    

    def addObject(self, gObject):
        '''Adds the object to the group'''
        self.objGroup.append(gObject)

    def move(self, dx, dy):
        '''Moves the entire face'''
        for obj in self.objGroup:
            obj.move(dx, dy)
        

    def draw(self, win):
        '''Draws the entire face with all objects'''

        for obj in self.objGroup:
            obj.draw(win)

    def undraw(self):
        '''Undraws the entire face'''
        for obj in self.objGroup:
            obj.undraw()


def main()->None:

    #win for face 
    win = GraphWin("Face", 600, 500)

    #anchor Point
    anchor = Point(300, 250)
    grp = GraphicsGroup(anchor)

    size = 100
    #face outline
    outline = Circle(Point(300, 250), size)
    grp.addObject(outline)

    #drawing eyes
    x = grp.getAnchor().getX()
    y = grp.getAnchor().getY()
    #left eye
    left_eye = Circle(Point(x-(size*0.5), (y-size*0.5)), size/10)
    left_eye.setFill("brown")
    grp.addObject(left_eye)
    

    #right eye
    right_eye = Circle(Point(x+(size*0.5), (y-size*0.5)), size/10)
    right_eye.setFill("brown")
    grp.addObject(right_eye)

    #Drawing mouth as two parts
    mouth_1 = Rectangle(Point(x-(size*0.5), y+(size*0.5)),Point(x+(size*0.5), y+(size*0.55)))
    mouth_1.setFill('black')
    mouth_1.setOutline('white')
    grp.addObject(mouth_1)

    mouth_2 = Rectangle(Point(x-(size*0.5), y+(size*0.55)),Point(x+(size*0.5), y+(size*0.6)))
    mouth_2.setFill('black')
    mouth_2.setOutline('white')
    grp.addObject(mouth_2)

    #drawinf all the objects
    grp.draw(win)

    #moving functionality
    while True:
        pt = win.getMouse()

        dx = pt.getX() - grp.getAnchor().getX()
        dy = pt.getY() - grp.getAnchor().getY()
        grp.move(dx, dy)

if __name__ == "__main__":
    main()


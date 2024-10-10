###Program: Click and type
from graphics import *

def handleKey(win, key):

    if key == 'w':
        win.setBackground("white")
    elif key == 'p':
        win.setBackground("pink")
    elif key == 'g':
        win.setBackground("green")
    elif key == 'l':
        win.setBackground("lightgray")
    elif key == 'f':
        win.setBackground("lightblue")


def handlePt(win, pt):
    pass #It does nothing as alternative for some statement

    
def main()->None:

    win = GraphWin("Click-type", 700, 600)

    

    while True:

        key = win.checkKey()

        if key == 'q':
            break

        if key:
            handleKey(win, key)

        pt = win.checkMouse()

        if pt:
            handlePt(win, pt)


    win.close()

main()

        


        

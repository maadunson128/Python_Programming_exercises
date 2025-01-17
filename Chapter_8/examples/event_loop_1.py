###Program: Changing the backgroung of window

from graphics import *

def main()->None:
    win = GraphWin("Background changer", 900, 700)

    #Event loop: Changes background nased Key pressed (Event: Key pressing)
    while True:
        key = win.getKey()

        if key == 'q':
            break

        elif key == 'g':
            win.setBackground("green")
        elif key == 'w':
            win.setBackground("white")
        elif key == 'p':
            win.setBackground("pink")
        elif key == 'k':
            win.setBackground("lightgray")

    #closing the window
    win.close()


main()

    

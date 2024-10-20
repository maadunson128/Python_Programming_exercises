###Program: Event loop
from graphics import *

#function to handle the keys pressed
def processKey(win, key)->None:
    if key == 'g':
        win.setBackground("gray")
    elif key == 'w':
        win.setBackground("white")
    elif key == 'r':
        win.setBackground("red")

#function to handle the mouse click
def processPt(win, pt)->None:
    entry = Entry(pt, 10)
    entry.draw(win)

    while True:
        key = win.getKey()
        if key == "Escape": break

    entry.undraw()
    typed = entry.getText()
    Text(pt, typed).draw(win)

    win.checkMouse()
    

    
def main()->None:

    win = GraphWin("Event loop", 600, 600)

    ##Event loop: Checks for keys and clicks
    while True:
        key = win.checkKey()

        if key == 'q':
            break

        if key:
            processKey(win, key)

        pt = win.checkMouse()

        if pt:
            processPt(win, pt)

    win.close()
        

main()

    

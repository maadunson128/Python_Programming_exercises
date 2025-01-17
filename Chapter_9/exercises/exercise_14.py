###Program: Random walk simulation

#importing modules
from random import randint
from graphics import *
import math

#info function
def info()->None:
    print("This is a simulation of random walking in graphical interface.")

def simWalk(n:int, win)->None:
    #initial positions
    old_point = Point(500, 500)
    for _ in range(n):
        angle:int = randint(0, 180) #random angle generation

        #calculating new x, y values
        new_x:int = old_point.getX() + math.cos(angle)
        new_y:int = old_point.getY() + math.sin(angle)
        
        new_point = Point(new_x, new_y)
        #drawing line between old and new point
        Line(old_point, new_point).draw(win)


        old_point = new_point #new point becomes as old

def main()->None:
    #info about the simulation
    info()

    #input: n number of steps
    n:int = int(input("Enter the number of steps to simulate: "))

    #graphical window
    win = GraphWin('Walking simulation', 1000, 1000) #the 100X100 grid is scaled up 10 times

    #simulating the walking
    simWalk(n, win)

main()

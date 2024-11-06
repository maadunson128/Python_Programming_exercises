###Program: Simulation of one dimensional random walk
from random import choice

#info about the simulation
def info()->None:
    print("This is a simulation of one dimensional random walk.")
    print("The direction of walking in steps is determined by random coin toss.")

#simulate each step
def simulateWalk(n:int)->None:
    #simulating for each step
    steps:int = 0 #initial point 0
    for _ in range(n):
        res:str = choice(['H', 'T'])  # steps forward or backward based on coin toss

        if res == 'H':
            steps += 1 #forward step
        elif res == 'T':
            steps -= 1 #backward step

    return abs(steps)
    
def main()->None:

    #info about the simulation
    info()

    #get input: number of steps
    n:int = int(input("Enter the number of steps: "))

    #simulate the walk
    avg_steps:int = simulateWalk(n)

    #result
    print(f"You are {avg_steps} steps from the initial point 0.")


main()

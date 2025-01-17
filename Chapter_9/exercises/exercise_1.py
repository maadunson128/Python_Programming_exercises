###Program: Simulating the Racquet Ball game

from random import random
#function for getting inputs
def getInputs()->tuple[float, float, int]:
    probA:float = float(input("Enter the probability of A will win out of total serves: "))
    probB:float = float(input("Enter the probability of B will win out of total serves: "))
    n:int = int(input("Enter the total number of games to simulate: "))

    return probA, probB, n


#function for printing the Introduction
def intro()->None:
    print(f"This program is a simulation for Racquet Ball game.")
    print(f"The program will ask for three inputs.")
    print(f"\t1.probA -> Probability that the player A will win of his/her total serves.")
    print(f"\t2.probB -> Probability that the player B will win of his/her total serves.")
    print(f"\t3.n -> Total numbers of games going to be simulated.")
    print("\nLastly, a report will be printed for the winning percentages of A and B.")

#function for checking if game is over
def gameOver(scoreA:int, scoreB:int)->bool:
    return scoreA == 15 or scoreB == 15

#function for simulating one game
def simOnegame(probA:float, probB:float, serving:str)->tuple[int, int]:
    scoreA:int = 0
    scoreB:int = 0
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                serving = 'B'
        if serving == 'B':
            if random() < probB:
                scoreB += 1
            else:
                serving = 'A'

    return scoreA, scoreB


#function for simulating the N games
def simNgames(probA:float, probB:float, n:int)->tuple[int, int]:
    winsA:int = 0
    winsB:int = 0
    for i in range(1, n+1):
        if i%2 == 0:
            scoreA, scoreB = simOnegame(probA, probB, 'B')
        else:
            scoreA, scoreB = simOnegame(probA, probB, 'A')

        if scoreA > scoreB:
            winsA += 1

        else:
            winsB += 1

    return winsA, winsB

#function for printing the report
def report(winsA:int, winsB:int, n:int)->None:
    print(f"Total number of games simulated: {n}")
    print(f"Percentage of Player A won: {winsA/n * 100}%")
    print(f"Percentage of Player B won: {winsB/n * 100}%")
    

    
def main()->None:

    #introduction
    intro()

    #getting inputs: probA, probB, n
    probA, probB, n = getInputs()

    #simulating the games
    winsA, winsB = simNgames(probA, probB, n)

    #printing the report of simulation
    report(winsA, winsB, n)


main()

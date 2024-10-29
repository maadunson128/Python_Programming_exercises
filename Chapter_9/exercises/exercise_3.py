###program: Simulation for Volleyball game

from random import random

#function to print the intro about the program
def intro()->None:
    print("This program will simulate N games for the Volleyball game.")
    print("The user have to give inputs below.")
    print("\t1. probA -> probability that the team A will win of their total serves.")
    print("\t2. probB -> probability that the team B will win of their total serves.")
    print("\t3. n -> total number of games to be simulate.")
    print("Finally, It will print the report of the simulation.")

#function to get inputs
def getInputs()->tuple[float, float, int]:
    probA:float = float(input("Enter the probability that the team A will win of total serves: "))
    probB:float = float(input("Enter the probability that the team B will win of total serves: "))
    n:int = int(input("Enter the total number of games to simulate: "))

    return probA, probB, n
#function for checking the game is over
def gameOver(scoreA:int, scoreB:int)->bool:
    return (abs(scoreA - scoreB) >= 2) and (scoreA >= 15 or scoreB >= 15)

#function to simulate one game
def simOneGame(probA:float, probB:float)->tuple[int, int]:
    scoreA:int = 0
    scoreB:int = 0
    #assuming the team A will serve first for each game.
    serving:str = 'A'
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = 'A'
    return scoreA, scoreB

        
#function to simulate N games
def simNgames(probA:float, probB:float, n:int)->tuple[int, int]:
    winsA:int = 0
    winsB:int = 0
    for i in range(1, n+1):
        scoreA, scoreB = simOneGame(probA, probB)

        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1

    return winsA, winsB

#printing the report
def report(winsA, winsB)->None:
    print("Total number of games simulated:",winsA+winsB)
    print("Total number of games team A won:", winsA)
    print("Percentage of Team A won in total games:", winsA/(winsA+winsB) * 100, "%")
    print("Total number of games team B won:", winsB)
    print("Percentage of Team B won in total games:", winsB/(winsA+winsB) * 100, "%")

    
def main()->None:

    #intro
    intro()

    #getting inputs: probA, probB, n
    probA, probB, n = getInputs()

    #simulating N volleyball games
    winsA, winsB = simNgames(probA, probB, n)

    #report printing
    report(winsA, winsB)


main()

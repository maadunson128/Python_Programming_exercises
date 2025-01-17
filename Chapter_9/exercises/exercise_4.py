###Program: Simulation of Volleyball game based on ralyy point system

from random import random

#function for printing the intro
def intro()->None:

    print("This program is a simulation of Volleyball games using Rally scoring.")
    print("The user will input the probability of winning of Teams A and B in their total serve and the number of games to simulate.")
    print("Finally, the program will print the report of the simulation.")

#function for getting inputs
def getInputs()->tuple[float, float, int]:
    probA:float = float(input("Enter the probbaility of team A will win in total serves: "))
    probB:float = float(input("Enter the probbaility of team B will win in total serves: "))
    n:int = int(input("Enter the total number of games to simulate: "))

    return probA, probB, n


#function to check if the game is over
def gameOver(scoreA:int, scoreB:int)->bool:
    return (abs(scoreA - scoreB) >= 2) and (scoreA >= 25 or scoreB >= 25)

#function to simulate one game
def simOneGame(probA:float, probB:float)->tuple[int, int]:
    scoreA:int = 0
    scoreB:int = 0
    serving = 'A' #assuming the team A will serve after each game
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA +=1
            else:
                scoreB += 1 #rally scoring
                serving = 'B'
        else:
            if random() < probB:
                scoreB += 1
            else:
                scoreA += 1 #rally scoring
                serving = 'A'

    return scoreA, scoreB
            
#function to simulate N games
def simNgames(probA:float, probB:float, n:int)->tuple[int, int]:
    winsA:int = 0
    winsB:int = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)

        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
            
    return winsA, winsB

#printing the report
def report(winsA, winsB)->None:
    print(f"Total number of games simulated: {winsA+winsB}")
    print(f"Total number of games team A won: {winsA}")
    print(f"Percentage of Team A won in total games: {winsA/(winsA+winsB) * 100}%")
    print(f"Total number of games team B won: {winsB}")
    print(f"Percentage of Team B won in total games: {winsB/(winsA+winsB) * 100}%")
    

def main()->None:

    #printing intro
    intro()

    #getting user inputs: probA, probB, n
    probA, probB, n = getInputs()

    #simulating N games
    winsA, winsB = simNgames(probA, probB, n)

    #printing the report
    report(winsA, winsB)


main()

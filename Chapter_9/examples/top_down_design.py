###Program: This program is simulation of Racquetball game implemented using top-down approach

#importing random module
from random import random

#function to print the intro
def intro()->None:
    print("This program will simulate the games with info the user will enter.")
    print("The user have to enter the value of probA (probablilty that player A will win out of total serves)")
    print("and probB(probability that B will win out of total serves. The user also input the value n (total matches to simulate).")

#function for getting input
def getInfo()->tuple[float, float, int]:
    probA:float = float(input("Enter the probability that A will win for total serves: "))
    probB:float = float(input("Enter the probability that B will win for total serves: "))
    n:int = int(input("Enter the total number of games: "))

    return probA, probB, n

#function to check gameOver Condition
def gameOver(scoreA, scoreB)->bool:
    return scoreA == 15 or scoreB == 15

#function to simulate one game
def simOneGame(probA:float, probB:float)->tuple[int, int]:
    serving:str = 'A'
    scoreA:int = 0
    scoreB:int = 0
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
    #print(f"Single game score: {scoreA}, {scoreB}")
    return scoreA, scoreB
                
    
#function to simulate the total games
def simNgames(probA:float, probB:float, n:int)->tuple[int, int]:
    '''This function simulates all the games and return the winning count of A and B'''
    winsA:int = 0
    winsB:int = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    #print(winsA, winsB)
    return winsA, winsB
        
#function to print the report
def printReport(winsA, winsB)->None:
    print(f"Total games simulated : {winsA+winsB}")
    print(f"Percentage of Player A won: {(winsA/(winsA + winsB))*100}%")
    print(f"Percentage of Player B won: {(winsB/(winsA + winsB))*100}%")
        

def main()->None:
    #intro to the program and its specification
    intro()

    #inputs from the user: probA, probB, n
    probA, probB, n = getInfo()

    #simulating the matches
    scoreA, scoreB = simNgames(probA, probB, n)

    #printing the report
    printReport(scoreA, scoreB)


main()
    

    
    

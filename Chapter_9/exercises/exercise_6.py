###Program: Simulation of Tennis

#importing random function
from random import random, choice

#funtion for checking of the any player wins earlier
def matchOver(setsA:int, setsB:int)->bool:
    return setsA == 3 or setsB == 3

    
#function for checking if game is over or not
def setOver(scoreA, scoreB)->bool:
    return (scoreA == 6 and scoreB == 6) or ((scoreA >= 6 or scoreB >= 6) and (abs(scoreA-scoreB) >=2))

#function to handle the tiebreak
def tiebreak(probA:float, probB:float, serving:str)->str:
    scoreA:int =0
    scoreB:int =0
    toggle:bool = True if serving == 'A' else False
    while not ((scoreA >= 7 or scoreB >= 7) and abs(scoreA - scoreB) >= 2): 
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                scoreB += 1
        else:
            if random() < probB:
                scoreB += 1
            else:
                scoreA += 1

        if (scoreA + scoreB) %2 != 0:
            toggle = not toggle
            serving = 'A' if toggle else 'B' #serving changes after each 2 points after 1st point

    return "A" if scoreA > scoreB else "B"


#function to handle if game over or not
def gameOver(scoreA, scoreB)->bool:
    return (scoreA >=4 or scoreB >= 4) and (abs(scoreA-scoreB) >= 2)


#function for simulating each game
def simOneGame(probA:float, probB:float, serving:str)->str:
    scoreA:int = 0
    scoreB:int = 0
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                scoreB += 1
                
        else:
            if random() < probB:
                scoreB += 1
            else:
                scoreA += 1
                
    return "A" if scoreA > scoreB else "B"

#function to simulate set
def simSet(probA:float, probB:float, serving:str)->str:
    gameScoreA:int = 0
    gameScoreB:int = 0
    #simualting each game in a set untill the game over
    while not setOver(gameScoreA, gameScoreB):
        winner = simOneGame(probA, probB, serving)
        serving = 'A' if serving == 'B' else 'B'

        if winner == 'A':
            gameScoreA += 1
        elif winner == 'B':
            gameScoreB += 1
    #print(gameScoreA, gameScoreB)
    if gameScoreA == 6 and gameScoreB == 6:
        return tiebreak(probA, probB, serving)
    elif gameScoreA > gameScoreB:
        return "A"
    elif gameScoreB > gameScoreA:
        return "B"
    
#function to simulate 5 sets
def sim5sets(probA:float, probB:float)->tuple[int, int]:
    setsA:int = 0
    setsB:int = 0
    winner:str = ''
    serve = choice(['A', 'B'])  #randomness for coin toss for first serve
    while not matchOver(setsA, setsB):
        #simulating each set
        winner = simSet(probA, probB, serve)
        serve = 'A' if serve == 'B' else 'B'  #serve change after each set
        if winner == 'A':
            setsA += 1
        elif winner == 'B':
            setsB += 1

    return setsA, setsB

#function to simulate N games
def simNgames(probA:float, probB:float, n:int)->tuple[int, int]:
    winA:int = 0
    winB:int = 0
    
    #simulating each set
    for i in range(n):
        setsA, setsB = sim5sets(probA, probB)  # we assuming the tennis consists of 5 sets

        if setsA > setsB:
            winA += 1
        else:
            winB += 1

    return winA, winB

#function to print the intro
def intro()->None:
    print("This is a tennis simulation.")
    print("The user have to input the probA (probability that Player A will win in total serves), probB\n(probability that Player \
           B will win in total serves), n(total number of games to simulate).")
    print("The simulation will give a report about the winnings at the end.")


#function to get the inputs
def getInputs()->tuple[float, float, int]:
    probA:float = float(input("Enter the probability that player A will win in total serves: "))
    probB:float = float(input("Enter the probability that player B will win in total serves: "))
    n:int = int(float(input("Enter the games to simulate: ")))
    return probA, probB, n 

#function to print the report
def report(winsA, winsB, n)->None:
    print("Total games simulated:", n)
    print(f"Player A wins out of total matches: {winsA}")
    print(f"Percentage of player A winnings: {winsA/n * 100}%")
    print(f"Player B wins out of total matches: {winsB}")
    print(f"Percentage of player B winnings: {winsB/n * 100}%")

def main()->None:

    #intro
    intro()

    #getting inputs
    probA, probB, n = getInputs()

    #simulating N games
    winA, winB = simNgames(probA, probB, n)

    #report
    report(winA, winB, n)

main()

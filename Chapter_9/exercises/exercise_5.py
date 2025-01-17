###Prpgram: Comparision of Normal Volley ball and with rally scoring
from random import random

#function for printing the intro
def intro()->None:
    print("This program will simulate the volley ball game and compare ot with rally scoring Volleyball game.")
    print("Note: The team A is considered as best team (Give value larger than team B)")

#function for getting inputs
def getInputs()->tuple[float, float, int]:
    probA:float = float(input("Enter the probability of team A will win in total serves: "))
    probB:float = float(input("Enter the probability of team B will win in total serves: "))
    n:int = int(input("Enter the total number of games to simulate and compare: "))
    
    return probA, probB, n


#function for checking gameover or not
def gameOver(scoreA, scoreB)->bool:
    return (abs(scoreA-scoreB) >= 2) and (scoreA >= 25 or scoreB >= 25)

#function for simulating normal volleyball
def simOneGame(probA:float, probB:float, game:str)->tuple[int, int]:
    serving:str = 'A' #Assuming that the team A will serve for each game
    scoreA:int = 0
    scoreB:int = 0
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                if game == 'Rally': scoreB += 1 #rally scoring
                serving = 'B'

        else:
            if random() < probB:
                scoreB += 1
            else:
                if game == 'Rally':scoreA += 1 #ralay scoring
                serving = 'A'

    return scoreA, scoreB


        
#function to simulate the N games
def simNgames(probA:float, probB:float, n:int)->tuple[int, int, int, int]:
    winAn:int = 0
    winBn:int = 0
    winAr:int = 0
    winBr:int = 0
    for i in range(n):
        #simulating each game for normal volleyball
        scoreAn, scoreBn = simOneGame(probA, probB, game='Normal')
        if scoreAn > scoreBn:
            winAn += 1
        else:
            winBn += 1

        #simulating each game for rally scoring volleyball
        scoreAr, scoreBr = simOneGame(probA, probB, game='Rally')
        if scoreAr > scoreBr:
            winAr += 1
        else:
            winBr += 1

    return winAn, winBn, winAr, winBr

#function for creating the table
def createTable(winAn, winBn, winAr, winBr, better_team)->None:
    #calculations
    perc_A_n:float = winAn/(winAn + winBn) * 100
    perc_A_r:float = winAr / (winAr+winBr) * 100
    perc_B_n:float = winBn/(winAn + winBn) * 100
    perc_B_r:float = winBr / (winAr+winBr) * 100

    #creating table
    print(f"\n{'Teams':^15} |  {'Percentage wins(Normal scoring)'}  |  {'Percentage wins(rally scoring)'}  ")
    print("-"*90)
    print(f"{'Team A':^15} |{perc_A_n:^35.4f}|{perc_A_r:34.4f} ")
    print("-"*90)
    print(f"{'Team B':^15} |{perc_B_n:^35.4f}|{perc_B_r:34.4f} ")


    #conclusion
    if better_team == 'A':
        minus_value:float = perc_A_n - perc_A_r
    elif better_team == 'B':
        minus_value:float = perc_B_n - perc_B_r
    if minus_value >= 0 and minus_value < 1: # assuming between 0-5% has no net advantage
        print(f"The better team {better_team} has no net advantage in both scorings.")
    elif minus_value >= 1:
        print(f"The better team {better_team} have more advantage in Normal scoring.")
    else:
        print(f"The better team {better_team} have reduced advantage in Normal scoring.")
        

#function for finding the better team
def find_better_team(probA:float, probB:float)->str:
    if probA == probB:
        return "Error"
    elif probA > probB:
        return "A"
    else:
        return "B"
    
def main()->None:

    #intro
    intro()

    while True:
        #getting inputs: probA, probB, n
        probA, probB, n = getInputs()

        #finding the better team
        better_team:str = find_better_team(probA, probB)

        if better_team == "Error":
            print("Please enter probablities that are not equal. Since we want a better team.")
            continue
        else:
            break

    #simulating N games bor both
    winAn, winBn, winAr, winBr = simNgames(probA, probB, n)

    #creating the table and conclusion
    createTable(winAn, winBn, winAr, winBr, better_team)


main()

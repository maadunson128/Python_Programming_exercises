###Program: craps game simulation

#importing random module
from random import randint

#information about the game
def intro()->None:
    print(f"This is a simulation of Craps game. You have to enter the number of games to simulate \
            and you will get the probabilty of winning the game.")

#gettting inputs
def getInputs()->int:
    n:int = int(input("Enter the number of games to simulate: "))
    return n

#function for simulating initial roll
def initial_roll()->tuple[str, int]:
    out:int = randint(1, 6) + randint(1, 6) #simulating random two dice rolls

    if out in [2, 3, 12]:return 'L', out
    elif out in [7, 11]: return 'W', out
    elif out in [4, 5, 6, 8, 9, 10]: return 'C', out

#function for point roll
def pointRoll(point:int)->int:
    while True:
        point:int = 0
        out = randint(1, 6) + randint(1, 6)

        if out == point:
            point = 1
            break
        elif out == 7:
            break

    return point
    
#function for simulating one craps game
def simOnegame()->int:
    result:str = ''
    point:int = 0
    result, point = initial_roll()
    if result == 'W': return 1
    elif result == 'L': return 0
    elif result == 'C': return pointRoll(point)
    
#function for simulating N games
def simNgames(n:int)->int:
    total_score:int = 0
    for i in range(n):
        total_score += simOnegame() #simulating each crap game

    return total_score

#printing report
def report(score:int, n:int)->None:
    print(f"Probability of winning of total games: {score/n:.4f}")
    print(f"Percentage of winning in {n} games: {score/n * 100:.4f} %")
            
    
def main()->None:
    #info about the game
    intro()

    #Inputs: n (number of games tot simulate)
    n = getInputs()

    #simulating N craps games
    score = simNgames(n)

    #report for final answer
    report(score, n)

main()

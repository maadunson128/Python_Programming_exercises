###Program: Blackjack game simulation for dealer

import random

#function for the program intro
def intro()->None:
    print("This program will give the probabilty of dealer will get busted in total games.")

    
#function for simulating each dealer game to find if busted or not
def simOneGame()->bool:
    hasAce:bool = False
    total:int = 0
    
    
    while True:
        card:int = random.randint(1, 13) # 10,11,12 -> Face cards(king, queen, jack)

        #initial scoring
        if card >=10:
            score = 10
        elif card == 1:
            score = 1
            hasAce = True
        else:
            score = card # cards and score(2-9)

        #Add card value to the total
        total += score

        #checking and chance for ace to add score as by 10
        if hasAce and total+10 <=21:
            adjusted_total:int = total + 10
        else:
            adjusted_total:int = total

        #checking if dealer is busted or not
        if 17 <= adjusted_total <= 21:
            return False  #dealer should stop
        elif adjusted_total > 21:
            return True  # dealer is busted
            


    
#function for simulating each game to find the times the dealer busted
def simNGames(n:int)->int:
    return sum(simOneGame() for _ in range(n))


def main()->None:
    #intro
    intro()

    #n: number of games to simulate
    n:int = 1000

    #simulating each games
    total_bust:float = simNGames(n)

    #result
    print(f"Probability that the dealer will bust: {total_bust/n}")


main()

###Program: Blackjack game simulation for dealer with cards from ace to 10

import random

#function for the program intro
def intro()->None:
    print("This program will give the probabilty of dealer will get busted in total games.")

    
#function for simulating each dealer game to find if busted or not
def simOneGame(starting_card:int)->bool:
    hasAce:bool = starting_card == 1
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
def black_jack_for_starts(n:int)->float:
    bust_probs = []

    for starting_card in range(1, 11):
        dealer_busts = sum(simOneGame(starting_card) for _ in range(n))
        bust_probs.append(dealer_busts/n)

    return bust_probs


def main()->None:
    #intro
    intro()

    #n: number of games to simulate
    n:int = 1000

    #simulating blackjack game by showing different score at starting
    bust_probs:float = black_jack_for_starts(n)

    for i, bust_prob in enumerate(bust_probs):
        card_name:str = ''
        if i == 0: card_name = 'Ace'
        else: card_name = str(i+1)
        print(f"Starting with {card_name}: Bust Probability = {bust_prob:.4f}")

    


main()

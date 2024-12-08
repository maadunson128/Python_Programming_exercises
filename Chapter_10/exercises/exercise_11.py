###Program: Cards class program
from random import randint, choice
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def value(self):
        if self.rank == 1:
            return 1
        elif self.rank in range(2,11):
            return self.rank
        elif self.rank in range(11,14):
            return 10
        
    def __str__(self):
        dict1 = {
            1:"Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
        }

        dict2 = {
            's': "Spades",
            'd': "Diamonds",
            'c': "Clubs",
            'h': "Hearts"
        }

        return dict1.get(self.rank, str(self.rank)) + " of " + dict2.get(self.suit)


def main()->None:

    n = int(input("Enter number of cards to be generated randomly: "))

    rank = randint(1,13)
    suit = choice(['s', 'h', 'c', 'd'])
    for i in range(n):
        card = Card(rank, suit)
        print(f"Card generated is {card} and its blackJack value is {card.value()}")
        

main()
###Program: Card game simulation

#from exercise_14 import MakeCard
from exercise_6 import shuffle
class MakeCard:
    def __init__(self, rank, suit):
        self.rank = int(rank)
        self.suit = suit

    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def getValue(self):
        if self.rank in range(1, 11):
            return self.rank
        elif self.rank in range(11, 14):
            return 10
        
    def getRankName(self):
        dict1 = {
                1:"Ace",
                11: "Jack",
                12: "Queen",
                13: "King"
            }
        
        return dict1.get(self.rank, str(self.rank))

    def getSuitName(self):
        dict2 = {
                's': "Spades",
                'c': "Clubs",
                'h': "Hearts",
                'd': "Diamonds"
                
            }
        return dict2.get(self.suit)

        
    def __str__(self):
            return self.getRankName() + " of " + self.getSuitName()
    
class Deck:
    def __init__(self):
        '''Creates a deck of card'''
        self.cards = []
        #Cards in standard order
        for rank in range(1, 14):
            for suit in ['s', 'c', 'h', 'd']:
                card = MakeCard(rank, suit)
                self.cards.append(card)
                a = MakeCard(rank, suit)
                print(a)
    
        

    def printCards(self):
        '''Print the cards with names'''
        for card in self.cards:
            print(card)


    def shuffle(self):
        '''Shuffles the cards list'''
        self.cards = shuffle(self.cards)

    def dealCard(self):
        '''Returns the Top card and removes from the list'''
        removed_card = self.cards.pop()
        

    def cardsLeft(self):
        '''Returns the number of cards left'''
        return len(self.cards)
    

def main()->None:
    cards = []
    for rank in range(1, 14):
            for suit in ['s', 'c', 'h', 'd']:
                card = MakeCard(rank, suit)
                cards.append(card)
                a = MakeCard(rank, suit)
                print(a)

    for card in cards:
        print(card)


if __name__ == "__main__":
    main()


                
        
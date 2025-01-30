###Program: Card game simulation
from random import shuffle
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
        self.cards = [MakeCard(rank, suit) for rank in range(1, 14) for suit in ['s', 'c', 'h', 'd']]

    def printCards(self):
        '''Print the cards with names'''
        for card in self.cards:
            print(card)


    def shuffle(self):
        '''Shuffles the cards list'''
        shuffle(self.cards)

    def dealCard(self):
        '''Returns the Top card and removes from the list'''
        return self.cards.pop()
        #print(f'Removed Card: {removed_card}')
        

    def cardsLeft(self):
        '''Returns the number of cards left'''
        return len(self.cards)
    
    def cardsHand(self):
        '''Returns 13 cards for a hand'''
        return [self.cards.pop() for _ in range(13)]

    
class BridgeHand:
    def __init__(self, handname, cards):
        '''Creates Hand'''
        self.cards = cards
        self.name = handname
        self.points = sum([card.getValue() for card in self.cards])

    def getOpeningBid(self):
        '''Gives opening bid for the hand'''
        if self.points >= 22:
            return "2C (Strong Artificial)"
        elif self.points >= 15:
            return "1NT (Balanced Hand)"
        elif self.points >= 13:
            return "1 of a Major/Minor"
        else:
            return "Pass"
        
    def showHand(self):
        '''Shows the hand with opening bid'''
        print(f"{self.name} Hand , {self.points} HCP")
        for card in self.cards:
            print(f" {card}")
        print(f"Opening Bid: {self.getOpeningBid()}\n")


class BridgeGame:
    def __init__(self):
        '''Creates things for bridge game'''
        self.deck = Deck()
        self.deck.shuffle()
        self.hands = {
            "North": BridgeHand("North", self.deck.cardsHand()),
            "South": BridgeHand("South", self.deck.cardsHand()),
            "East": BridgeHand("East", self.deck.cardsHand()),
            "West": BridgeHand("West", self.deck.cardsHand())

        }

    def playGame(self):
        '''Each player shows their opening bids and cards they have'''
        print("Welcome to Bridge Hand game")
        for hand in self.hands.values():
            hand.showHand()



if __name__ == "__main__":
    game = BridgeGame()
    game.playGame()
    



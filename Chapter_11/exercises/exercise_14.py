###Program: Cards sorter
class MakeCard:
    def __init__(self, rank, suit):
        self.rank = rank
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
                'd': "Diamonds",
                'c': "Clubs",
                'h': "Hearts"
            }
        return dict2.get(self.suit)

        
    def __str__(self):
            return self.getRankName() + " of " + self.getSuitName()
        


def checkRoyalFlush(cards):
    suits = [x.getSuit() for x in cards]
    ranks = [y.getRank() for y in cards]

    
    return sorted(ranks) ==  ['1', '10', '11', '12', '13'] and all(suit==suits[0] for suit in suits)
  

def checkStraightFlush(cards):
    '''Straight Flush Five ranks in a row, all of the same suit.'''
    suits = [x.getSuit() for x in cards]
    ranks = sorted([int(y.getRank()) for y in cards])

    return all(suit == suits[0] for suit in suits) and (ranks == list(range(ranks[0], ranks[0]+5)))

    
def checkFourKind(cards):
    '''Four of a Kind Four of the same rank.'''

    ranks = [int(y.getRank()) for y in cards]

    dict_count = {}
    for rank in ranks:
        dict_count[rank] = dict_count.get(rank, 0) + 1

    return  4 in dict_count.values()

def checkFullHouse(cards):
    '''Three of one rank and two of another.'''

    ranks = [int(y.getRank()) for y in cards]

    dict_count = {}
    for rank in ranks:
        dict_count[rank] = dict_count.get(rank, 0) + 1

    return 3 in dict_count.values() and 2 in dict_count.values()

def checkFlush(cards):
    '''Flush Five cards of the same suit.'''
    suits = [card.getSuit() for card in cards]
    
    return all([suits == list(suits[0] for _ in range(len(suits)))])


def checkStraight(cards):
    '''Straight Five ranks in a row. '''
    
    ranks = sorted([int(card.getRank()) for card in cards])

    return ranks == list(range(ranks[0], ranks[0]+5))

def checkThreeKind(cards):
    '''Three of a kind Three of one rank (but not a full house or four of a kind) .'''
    ranks = [int(y.getRank()) for y in cards]

    dict_count = {}
    for rank in ranks:
        dict_count[rank] = dict_count.get(rank, 0) + 1

    return  3 in dict_count.values() and (not checkFullHouse(cards)) and (not checkFourKind(cards))

def checkTwoPair(cards):
    '''Two pair Two each of two different ranks.'''

    ranks = [int(y.getRank()) for y in cards]

    dict_count = {}
    for rank in ranks:
        dict_count[rank] = dict_count.get(rank, 0) + 1

    return list(dict_count.values()).count(2) == 2

def checkPair(cards):
    '''Pair Two of the same rank (but not two pair, three or four of a kind).'''

    ranks = [int(y.getRank()) for y in cards]

    dict_count = {}
    for rank in ranks:
        dict_count[rank] = dict_count.get(rank, 0) + 1

    return (2 in dict_count.values()) and \
            (not checkTwoPair(cards))and \
            (not checkFourKind(cards))and \
            (not checkThreeKind(cards))

def checkXHigh(cards):
    '''X High If none of the previous categories fit, X is the value of the highest 
        rank. For example, if the largest rank is 1 1, the hand is 'jack high.'''
    
    ranks = [int(y.getRank()) for y in cards]
    x_high = max(ranks)

    dict1 = {
                1:"Ace",
                11: "Jack",
                12: "Queen",
                13: "King"
            }
    x_high = dict1.get(x_high, str(x_high))


    return x_high + " High"



def main()->None:

    #input file for cards ranks and suit
    infile = open("input_14.txt", 'r')

    cards = []
    for line in infile:
        rank, suit = line.split()
        cards.append(MakeCard(rank, suit))

    cards.sort(key=MakeCard.getRank)
    cards.sort(key=MakeCard.getSuit)

    for card in cards:
        print(card)


    #categorising the five cards
    if checkRoyalFlush(cards):
        print("Category: Royal Flush")
    elif checkStraightFlush(cards):
        print("Category: Straight Flush")
    elif checkFourKind(cards):
        print("Category: Four of a kind")
    elif checkFullHouse(cards):
        print("Category: Full House")
    elif checkFlush(cards):
        print("Category: Flush")
    elif checkStraight(cards):
        print("Category: Straight")
    elif checkThreeKind(cards):
        print("Category: Three of a kind")
    elif checkTwoPair(cards):
        print("Category: Two Pair")
    elif checkPair(cards):
        print("Category: Pair")
    else:
        print(f"Category: {checkXHigh(cards)}")
    

if __name__ == "__main__":
    main()


    


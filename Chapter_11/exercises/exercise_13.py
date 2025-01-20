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

    #input file for cards ranks and suit
    infile = open("input_13.txt", 'r')

    cards = []
    for line in infile:
        rank, suit = line.split()
        cards.append(MakeCard(rank, suit))

    cards.sort(key=MakeCard.getRank)
    cards.sort(key=MakeCard.getSuit)

    for card in cards:
        print(card)


if __name__ == "__main__":
    main()


    


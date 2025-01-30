###Program: War game

from exercise_6 import MakeCard, Deck


class Player:
    def __init__(self, name):
        'Makes player for the war game'
        self.cards = []
        self.name = name

    def addCards(self, cards):
        'Add won cards to the player'
        self.cards.extend(cards)

    def drawCard(self):
        'Draws the card for playing game'
        return self.cards.pop()



class WarGame:
    def __init__(self):
        print("Welcome to the War Game!!!")
        self.p1 = input("Enter player 1 name: ")
        self.p2 = input("Enter player 2 name: ")
        self.player1 = Player(self.p1)
        self.player2 = Player(self.p2)
        self.deck = Deck()
        self.deck.shuffle()
        self.distributeCards()
        print(f"Cards has been distributed to players {self.p1} and {self.p2}")
        self.p1_wins = 0
        self.p2_wins = 0

    def distributeCards(self):
        '''Distribute cards to players'''
        while self.deck.cards:
            self.player1.cards.append(self.deck.dealCard())
            self.player2.cards.append(self.deck.dealCard())
        
    def playRound(self):
        '''Plays a single round of game'''
        if not self.player1.cards or not self.player2.cards:
            return False
        
        card1 = self.player1.drawCard()
        card2 = self.player2.drawCard()
        print(f"Player 1 draws card {card1}")
        print(f"Player 2 draws card {card2}")

        if card1.getValue() > card2.getValue():
            self.player1.addCards([card1, card2])
            print(f"{self.p1} win the round")
            self.p1_wins += 1
        elif card1.getValue() < card2.getValue():
            self.player2.addCards([card1, card2])
            print(f"{self.p2} win the round")
            self.p2_wins +=1
        else:
            print("No one wins.It's a tie!!!!")

        return True
    
    def playGame(self):
        '''Plays the war game'''
        while True:
            if not self.playRound():
                break

            print("Please <Enter> to continue to next Round!!!\n")
            input()

        print(f"Rounds won by {self.p1}: {self.p1_wins}")
        print(f"Rounds won by {self.p2}: {self.p2_wins}")

        if self.p1_wins > self.p2_wins:
            print(f"{self.p1} won the game")
        elif self.p1_wins < self.p2_wins:
            print(f"{self.p1} won the game")
        else:
            print("No one wins the game. Its tie and occurs very raree!!!!!!")


if __name__ == "__main__":
    game = WarGame()
    game.playGame()







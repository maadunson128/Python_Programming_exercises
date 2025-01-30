###Program: Racquet Ball game simulation using OOD
from random import random
class SimStats:
    def __init__(self):
        '''Stats about the wins and shutouts of Player A and B'''
        self.winsA = 0
        self.winsB = 0
        self.shutsA = 0
        self.shutsB = 0

    def update(self, game):
        '''Update the values of stats according the game played'''
        scoreA, scoreB = game.getScore()
        if scoreA > scoreB:         # A wins
            self.winsA += 1
            if scoreB == 0:
                self.shutsA += 1
        elif scoreB > scoreA:       # B wins
            self.winsB += 1
            if scoreA == 0:
                self.shutsB += 1

    
    def printReport(self):
        '''Prints a nicely formatted report'''
        n = self.winsA + self.winsB
        print(f"Summary of {n} games")
        print("           wins  (%total)     shutouts   (%wins)")
        print("---------------------------------------------")
        self.printLine("A", self.winsA, self.shutsA, n)
        self.printLine("B", self.winsB, self.shutsB, n)

    
    def printLine(self, player, wins, shutouts, totalGames):
        '''Helps to print line in nice format'''
        shutstr = ''
        template = "Player {0}:{1:5}   {2:5.1%}   {3:12}  {4}"
        if wins == 0:
            shutstr = "   ----  "
        else:
            shutstr = "{0:6.1%}".format(float(shutouts)/wins)

        print(template.format(player, wins, float(wins)/totalGames, shutouts, shutstr))


class RGame:
    def __init__(self, probA, probB):
        '''Creates a game for Raquet ball game'''
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA

    def play(self):
        '''PLays the game untill the game over'''
        while not self.isOver():
            if self.server.winsServe():
                self.server.incScore()
            else:
                self.changeServe()

    def getScore(self):
        '''Returns the score of the player'''
        return self.playerA.getScore(), self.playerB.getScore()
    
    def changeServe(self):
        '''Changes the serve'''
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA

    def isOver(self):
        '''Checks if the game over or not'''
        a, b = self.getScore()
        return (a == 15 or b == 15) or \
                (a==7 and b == 0)  or (a==0 and b ==7)
    

class Player:
    def __init__(self, prob):
        '''Creates a player'''
        self.prob = prob
        self.score = 0
        
    def winsServe(self):
        '''Checks if the player wins the serve'''
        return random() < self.prob

    def incScore(self):
        self.score += 1

    def getScore(self):
        '''Returns the score of the player'''
        return self.score
    
def printIntro():
    '''Inroduction print'''
    print("This is a racquet ball simulation based probablities.")
    print("Game is between two players A and B")
    print("You have to enter the probabilities of A and B")
    print("You will see a report of games simulated \n")

def getInputs():
    '''Getting inputs from the users'''
    probA = float(input("Enter the probability of A: "))
    probB = float(input("Enter the probability of B: "))
    n = int(input("Enter the games to be simulated: "))

    return probA, probB, n


def main()->None:
    printIntro()
    probA, probB, n = getInputs()
    stats = SimStats()
    for i in range(n):
        game = RGame(probA, probB)
        game.play()
        stats.update(game)

    #print the results
    stats.printReport()


if __name__ == "__main__":
    main()
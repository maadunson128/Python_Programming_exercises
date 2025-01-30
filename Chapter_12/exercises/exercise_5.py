###Program: Shunk Game

import random

class Dice:
    """Represents a six-sided die."""
    def roll(self):
        return random.randint(1, 6)

class Player:
    """Represents a player in the Skunk game."""
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.round_score = 0

    def reset_round_score(self):
        self.round_score = 0

    def add_to_total(self):
        self.total_score += self.round_score
        self.reset_round_score()

    def __str__(self):
        return f"{self.name}: Total Score = {self.total_score}"

class SkunkGame:
    """Represents the Skunk game."""
    def __init__(self, players):
        self.players = players
        self.dice = [Dice(), Dice()]
        self.rounds = ["S", "K", "U", "N", "K"]

    def play_round(self, round_name):
        print(f"\nRound {round_name}")
        for player in self.players:
            print(f"\n{player.name}'s turn!")
            player.reset_round_score()
            while True:
                choice = input("Roll or Hold? (r/h): ").strip().lower()
                if choice == 'h':
                    player.add_to_total()
                    print(f"{player.name} holds. Round score added to total.")
                    break
                elif choice == 'r':
                    die1, die2 = self.dice[0].roll(), self.dice[1].roll()
                    print(f"{player.name} rolled: {die1} and {die2}")
                    if die1 == 1 and die2 == 1:
                        print("Snake eyes! You lose all points in the game!")
                        player.total_score = 0
                        player.reset_round_score()
                        break
                    elif die1 == 1 or die2 == 1:
                        print("You rolled a 1. You lose points for this round!")
                        player.reset_round_score()
                        break
                    else:
                        player.round_score += die1 + die2
                        print(f"Round score: {player.round_score}, Total score: {player.total_score}")
                else:
                    print("Invalid choice. Please enter 'r' to roll or 'h' to hold.")

    def play_game(self):
        print("Welcome to Skunk!")
        for round_name in self.rounds:
            self.play_round(round_name)
            self.display_scores()
        self.declare_winner()

    def display_scores(self):
        print("\n--- Current Scores ---")
        for player in self.players:
            print(player)

    def declare_winner(self):
        print("\n--- Final Scores ---")
        self.display_scores()
        winner = max(self.players, key=lambda p: p.total_score)
        print(f"\nCongratulations, {winner.name}! You won with {winner.total_score} points!")

# Main program
if __name__ == "__main__":
    players = [Player("Alice"), Player("Bob")]  # Add more players if desired
    game = SkunkGame(players)
    game.play_game()
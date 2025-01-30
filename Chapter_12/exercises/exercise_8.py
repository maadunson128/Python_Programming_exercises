###Program: Interactive Connect Four game

class Board:
    def __init__(self, rows = 6, columns=7):
        '''Creates the layout for board'''
        self.rows = rows
        self.columns = columns
        self.grid = [[" " for _ in range(columns)] for _ in range(rows)]

    def displayBoard(self):
        '''Displays the Board'''
        for row in self.grid:
            print('|'.join(row))
            print('-' * (2 * self.columns-1))

    def dropDisc(self, column, dicsValue):
        '''Checks if the board has entered value if not put that disc'''
        for row in reversed(self.grid):
            if row[column] == ' ':
                row[column] = dicsValue
                return True
        return False
    
    def checkWinner(self, disc):
        '''Checks for winning connection (Horizontal, Vertical, and Diagonal)'''
        for row in range(self.rows):
            for col in range(self.columns):
                if self.checkDirection(row, col, 1, 0, disc) or \
                   self.checkDirection(row, col, 0, 1, disc) or \
                   self.checkDirection(row, col, 1, 1, disc) or \
                   self.checkDirection(row, col, 1, -1, disc):
                    return True
        return False

    def checkDirection(self, row, col, row_step, col_step, disc):
        '''Checks for connections in every way'''
        count = 0
        for _ in range(4):
            if 0 <= row < self.rows and 0 <= col < self.columns and self.grid[row][col] == disc:
                count += 1
            else:
                break
            row += row_step
            col += col_step
        return count == 4

    def isFull(self):
        '''Checks for the board is full'''
        return all(self.grid[0][col] != ' ' for col in range(self.columns))
    
class Player:
    def __init__(self, name, disc):
        '''Creates player with their name and chosen disc'''
        self.name = name
        self.disc = disc



class ConnectFour:
    def __init__(self):
        '''Creates board and player for the game'''
        print("Welcome to the Connect Four game")

        rows = int(input("Enter no of rows for the board(Min 4): "))
        self.columns = int(input("Enteer no of columns for the board (Min 4): "))
        self.board = Board(rows, self.columns+1)

        self.p1 = input("Enter player 1 name: ")
        self.p2 = input("Enter player 2 name: ")
        print(f"Player 1 {self.p1} disc: X \n Player 2 {self.p2} disc: O")
        self.players = [Player(self.p1, "X"), Player(self.p2, "O")]

        self.current_player_index = 0

    def switch_player(self):
        '''Switches player'''
        self.current_player_index = 1 - self.current_player_index

    def play_game(self):
        '''Main playing algo for the game'''
        while True:
            self.board.displayBoard()
            current_player = self.players[self.current_player_index]
            print(f"{current_player.name}'s turn ({current_player.disc}):")
            
            try:
                column = int(input(f"Enter a column (0-{self.columns}): "))
                if column < 0 or column >= self.board.columns or not self.board.dropDisc(column, current_player.disc):
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Enter a number between 0 and {self.columns}.")
                continue

            if self.board.checkWinner(current_player.disc):
                self.board.displayBoard()
                print(f"Congratulations {current_player.name}, you win!")
                break

            if self.board.isFull():
                self.board.displayBoard()
                print("The game is a tie!")
                break

            self.switch_player()


if __name__ == "__main__":
    game = ConnectFour()
    game.play_game()
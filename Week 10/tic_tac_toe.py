class Board:
    # Handles new board
    def __init__(self):
        self.__grid= [[' ' for _ in range(3)] for _ in range(3)]
    def display(self):
        print("Showing the grid")
        for row in self.__grid:
            print(" | ".join(row))
            print("_"*10)
    def update_square(self, row, col, symbol):
        """Update board only if empty."""
        if self.__grid[row][col] == ' ':
            self.__grid[row][col] = symbol
            return True
        return False

    def is_full(self):
        """Check if board is full."""
        return all(cell != ' ' for row in self.__grid for cell in row)

    def check_winner(self):
        """Check rows, columns, and diagonals for a win."""
        g = self.__grid
        for i in range(3):
            if g[i][0] == g[i][1] == g[i][2] != ' ':
                return True
            if g[0][i] == g[1][i] == g[2][i] != ' ':
                return True
            if g[0][0] == g[1][1] == g[2][2] != ' ':
                return True
            if g[0][2] == g[1][1] == g[2][0] != ' ':
                return True
        return False 

       
class Player:
    def __init__(self, name,symbol):
        self.symbol=symbol
        self.name=name
    
class Game:
    def __init__(self):
        print("Welcome to Tic-Tac-Toe!\n")

        name1 = input("Enter Player 1 name: ")
        name2 = input("Enter Player 2 name: ")

        self.player1 = Player(name1, 'X')
        self.player2 = Player(name2, 'O')
        self.board = Board()
        self.current_player = self.player1

    def other_player(self):
        """Switch players."""
        self.current_player = (
            self.player1 if self.current_player == self.player2 else self.player2
        )

    def play_one_turn(self):
        """Handle one player's move."""
        while True:
            try:
                row = int(input(f"{self.current_player.name}, enter row (0-2): "))
                col = int(input(f"{self.current_player.name}, enter column (0-2): "))

                if 0 <= row < 3 and 0 <= col < 3:
                    if self.board.update_square(row, col, self.current_player.symbol):
                        break
                    else:
                        print(" That square is already taken. Try again.")
                else:
                    print("Invalid range. Choose between 0–2.")
            except ValueError:
                print("Please enter valid numbers only!")

    def play_game(self):
        """Main game loop."""
        while True:
            self.board.display()
            self.play_one_turn()

            if self.board.check_winner():
                self.board.display()
                print(f" {self.current_player.name} wins the game!")
                break

            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break

            self.other_player()

def main():
    game=Game()
    game.play_game()
if __name__=="__main__":
    main()
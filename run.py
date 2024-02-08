import random
import os
import sys

# Define the board size and number of mines
BOARD_SIZE = 8
NUM_MINES = 10

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [["." for _ in range(size)] for _ in range(size)]
        self.mines = []
        self.start = (0, 0)
        self.goal = (size - 1, size - 1)

    def print_board(self, reveal=False):
        print("  " + " ".join(str(i) for i in range(self.size)))
        for idx, row in enumerate(self.board):
            row_to_print = row[:]
            if not reveal:
                row_to_print[self.goal[1]] = "G"  # Goal position
                if idx == self.start[0]:
                    row_to_print[self.start[1]] = "S"  # Start position
            print(idx, " ".join(row_to_print))

    def add_mines(self):
        while len(self.mines) < NUM_MINES:
            position = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            if position not in self.mines and position != self.start and position != self.goal:
                self.mines.append(position)
                self.board[position[0]][position[1]] = "*"  # Only for debugging purposes

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input():
    try:
        x = int(input(f"Enter row number (0 to {BOARD_SIZE - 1}): "))
        y = int(input(f"Enter column number (0 to {BOARD_SIZE - 1}): "))
        if x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE:
            print("Coordinates out of bounds. Please try again.")
            return get_user_input()
        return x, y
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return get_user_input()

def main():
    board = Board(BOARD_SIZE)
    board.add_mines()

    player_position = board.start

    clear_screen()

    print("Welcome to the Minefield!")
    print("Navigate from S (start) to G (goal) without stepping on a mine.")
    board.print_board(reveal=False)  

    while player_position != board.goal:
        x, y = get_user_input()

        if (x, y) in board.mines:
            print("Boom! You stepped on a mine. Game Over.")
            board.print_board(reveal=True)
            sys.exit()
        elif (x, y) == player_position:
            print("You are already at this position. Please try a different move.")
        else:
            player_position = (x, y)
            clear_screen()
            print(f"Moved to position {player_position}.")

        board.print_board(reveal=False)

    print("Congratulations! You've safely reached the goal!")

if __name__ == "__main__":
    main()

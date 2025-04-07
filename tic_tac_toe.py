
import time
import math

# Create the board
def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")

# Check if a player has won
def check_win(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Check if board is full
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Get player's move
def get_move(player):
    while True:
        try:
            row = int(input(f"{player}'s turn. Enter row (0-2): "))
            col = int(input(f"{player}'s turn. Enter column (0-2): "))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Please enter numbers only.")

# Main game loop
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row, col = get_move(current_player)

        if board[row][col] != ' ':
            print("Cell already taken! Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"{current_player} wins!")
            break

        if is_full(board):
            print("It's a tie!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'
        time.sleep(0.5)

play_game()
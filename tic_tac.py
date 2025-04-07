
import math

def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
    print()

def is_winner(board, player):
    # Rows, columns, diagonals
    for row in board:
        if all([spot == player for spot in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]):
        return True

    if all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    elif is_winner(board, 'X'):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for (r, c) in get_empty_cells(board):
            board[r][c] = 'O'
            score = minimax(board, depth + 1, False)
            board[r][c] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for (r, c) in get_empty_cells(board):
            board[r][c] = 'X'
            score = minimax(board, depth + 1, True)
            board[r][c] = ' '
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for (r, c) in get_empty_cells(board):
        board[r][c] = 'O'
        score = minimax(board, 0, False)
        board[r][c] = ' '
        if score > best_score:
            best_score = score
            move = (r, c)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe AI (You: X, AI: O)")
    print_board(board)

    while True:
        # Player move
        while True:
            try:
                row_input = input("Your move - Enter row (0-2) or 'q' to quit: ")
                if row_input.lower() == 'q':
                    print("Game exited.")
                    return
                col_input = input("Your move - Enter column (0-2) or 'q' to quit: ")
                if col_input.lower() == 'q':
                    print("Game exited.")
                    return

                row = int(row_input)
                col = int(col_input)

                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Cell already taken! Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers 0-2.")

        print_board(board)

        if is_winner(board, 'X'):
            print("🎉 You win!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        # AI move
        print("AI is thinking...")
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = 'O'
        print_board(board)

        if is_winner(board, 'O'):
            print("💻 AI wins! Better luck next time.")
            break
        elif is_full(board):
            print("It's a tie!")
            break

play_game()

     
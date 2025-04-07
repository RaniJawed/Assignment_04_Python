
from typing import List, Tuple, Optional

# Define a sample Sudoku board (0 represents empty cells)
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Function to print the board nicely
def print_board(bo: List[List[int]]) -> None:
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(bo[i][j] if bo[i][j] != 0 else ".", end=" ")
        print()

# Function to find the next empty cell
def find_empty(bo: List[List[int]]) -> Optional[Tuple[int, int]]:
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None

# Function to check if a number is valid at a given position
def is_valid(bo: List[List[int]], num: int, pos: Tuple[int, int]) -> bool:
    row, col = pos

    # Check row
    if any(bo[row][i] == num and col != i for i in range(len(bo[0]))):
        return False

    # Check column
    if any(bo[i][col] == num and row != i for i in range(len(bo))):
        return False

    # Check box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

# The main solving function using backtracking
def solve(bo: List[List[int]]) -> bool:
    find = find_empty(bo)
    if not find:
        return True  # Solved
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(bo, num, (row, col)):
            bo[row][col] = num

            if solve(bo):
                return True

            bo[row][col] = 0  # Backtrack

    return False

# Run the solver
print("🧩 Initial Sudoku Board:\n")
print_board(board)

if solve(board):
    print("\n✅ Solved Sudoku Board:\n")
    print_board(board)
else:
    print("\n❌ No solution exists.")
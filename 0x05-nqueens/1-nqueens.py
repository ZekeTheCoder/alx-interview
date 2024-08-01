#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.
This is a program that solves the N queens problem.
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at the position board[row][col].

    This function checks if placing a queen at the given position (row, col)
    is safe from any attacks by other queens already placed on the board.
    Specifically, it ensures that no other queen is in:
    1. The same column.
    2. The same upper-left diagonal.
    3. The same upper-right diagonal.

    Parameters:
    - board (list of list of int): The 2D list representing the chessboard,
      where 1 indicates a queen and 0 indicates an empty space.
    - row (int): The row index where we want to place the queen.
    - col (int): The column index where we want to place the queen.

    Returns:
    - bool: True if it is safe to place a queen at (row, col), otherwise False.
    """

    # Check the column for any queens in previous rows
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal for any queens
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the upper-right diagonal for any queens
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    # no queens are found in the same column or diagonals
    return True


def backtrack_solutions(board, row, solutions):
    """
    Solve the N Queens problem using backtracking.

    Function uses a backtracking algorithm to place queens on the chessboard
    in a way that no two queens threaten each other. It explores all possible
    placements of queens row by row, and if it finds a valid configuration,
    it adds it to the solutions list.

    Parameters:
    - board (list of list of int): The 2D list representing the chessboard,
      where 1 indicates a queen and 0 indicates an empty space.
    - row (int): The current row index where we are trying to place a queen.
    - solutions (list of list of list of int): A list where each element is a
      valid solution (a list of queen positions) to the N Queens problem.

    Returns:
    - None: This function modifies the `solutions` list in place.
    """

    # If all rows processed, add the current board configuration to solutions
    if row >= len(board):
        solution = []
        # Extract positions of queens from the board configuration
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    # Try placing a queen in every column of the current row
    for col in range(len(board)):
        if is_safe(board, row, col):  # Check if it's safe to place a queen
            board[row][col] = 1       # Place the queen
            # Recur to place queens in the next row
            backtrack_solutions(board, row + 1, solutions)
            board[row][col] = 0       # Backtrack and remove the queen


def solve_n_queens(n):
    """
    Initialize the board and solve the N Queens problem using backtracking.

    Parameters:
    - n (int): size of chessboard (N) and the number of queens to be placed.

    Returns:
    - list of list of list of int: list where each element is a valid solution
      to the N Queens problem. Each solution is represented as a list of queen
      positions, where each position is a pair [row, col].
    """
    # Initialize the board with all zeros
    board = []
    for _ in range(n):
        row = [0] * n
        board.append(row)

    # List to store all valid solutions
    solutions = []

    # Start the backtracking process to find all solutions
    backtrack_solutions(board, 0, solutions)

    # Return the list of solutions
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

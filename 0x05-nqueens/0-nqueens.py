#!/usr/bin/python3
"""
This program solves the N-Queens problem using a backtracking algorithm
and prints all valid solutions.
"""

import sys


def print_chessboard(queen_positions, board_size):
    """
    Print the chessboard with queens placed at the given positions.

    Args:
    - queen_positions (list of int): A list where the index represents the row,
      and value at that index represents the column where a queen is placed.
    - board_size (int): The size of the chessboard (N).

    Prints:
    - Positions of all queens on the chessboard as a list of [row, col] pairs.
    """

    board = []
    for row in range(board_size):
        # Place each queen on the board based on its position
        col = queen_positions[row]
        board.append([row, col])

    print(board)


def is_safe(queen_positions, current_row, current_col, board_size):
    """
    Check if placing a queen at (current_row,current_col) is safe from attacks.

    Args:
    - queen_positions (list of int): A list where the index represents the row,
      and value at that index represents the column where a queen is placed.
    - current_row (int): The row index where we want to place the queen.
    - current_col (int): The column index where we want to place the queen.
    - board_size (int): The size of the chessboard (N).

    Returns:
    - bool: True if it is safe to place a queen at (current_row, current_col),
      otherwise False.

    Checks for:
    - Same column.
    - Same upper-left diagonal.
    - Same upper-right diagonal.
    """

    for row in range(current_row):
        col = queen_positions[row]
        if col == current_col or \
           col - row == current_col - current_row or \
           col + row == current_col + current_row:
            return False
    return True


def solve_nqueens(queen_positions, current_row, board_size):
    """
    Recursively find all valid placements for queens using backtracking.

    Args:
    - queen_positions (list of int): A list where the index represents the row,
      and value at that index represents the column where a queen is placed.
    - current_row(int): current row index where we are trying to place a queen.
    - board_size (int): The size of the chessboard (N).

    Modifies:
    - Prints all valid configurations of queens on the chessboard.
    """

    if current_row == board_size:
        print_chessboard(queen_positions, board_size)
    else:
        for col in range(board_size):
            if is_safe(queen_positions, current_row, col, board_size):
                queen_positions[current_row] = col
                solve_nqueens(queen_positions, current_row + 1, board_size)


def initialize_board(size):
    """
    Initialize a chessboard of given size with all positions set to 0.

    Args:
    - size (int): The size of the chessboard (N).

    Returns:
    - list of int: A list of size `size` initialized with zeros.
    """

    return [0] * size


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if board_size < 4:
        print("N must be at least 4")
        exit(1)

    queen_positions = initialize_board(board_size)
    solve_nqueens(queen_positions, 0, board_size)

#!/usr/bin/env python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.
This is a program that solves the N queens problem.
"""
import sys


def print_chessboard(queen_positions, board_size):
    """Print the chessboard with queens placed at the given positions"""

    board = []
    for row in range(board_size):
        for col in range(board_size):
            if col == queen_positions[row]:
                board.append([row, col])

    print(board)


def is_safe(queen_positions, current_row, current_col, board_size):
    """Check if placing a queen at (current_row, current_col) is safe"""

    for row in range(current_row):
        col = queen_positions[row]
        if col == current_col or \
           col - row == current_col - current_row or \
           col + row == current_col + current_row:
            return False
    return True


def solve_nqueens(queen_positions, current_row, board_size):
    """Recursive function to find all safe positions for queens"""

    if current_row == board_size:
        print_chessboard(queen_positions, board_size)
    else:
        for col in range(board_size):
            if is_safe(queen_positions, current_row, col, board_size):
                queen_positions[current_row] = col
                solve_nqueens(queen_positions, current_row + 1, board_size)


def initialize_board(size):
    """Function to create an empty chessboard of given size"""

    return [0] * size


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

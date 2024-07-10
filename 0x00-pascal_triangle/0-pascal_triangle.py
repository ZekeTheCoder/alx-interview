#!/usr/bin/python3
"""
This script has a function that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    # Initialize the Triangle
    triangle = []

    # Check for Non-Positive Input & return empty list if true
    if n <= 0:
        return triangle

    # Outer loop (generate each row of the triangle)
    for i in range(n):
        # initilize to 0 after each iteration
        current_row = []

        # inner loop (generate each element in current row)
        for j in range(i + 1):
            # checks to add [1] to first or last element of the row
            if j == 0 or j == i:
                current_row.append(1)
            else:
                # adds previous row elements using indices
                current_row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # adds current row to the triangle
        triangle.append(current_row)

    return triangle

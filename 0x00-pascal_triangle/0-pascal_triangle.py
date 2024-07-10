#!/usr/bin/python3
"""This script has a function that returns a list of lists of integers representing the Pascal’s triangle of n"""

def pascal_triangle(n):
    triangle = []
    
    # returns empty list
    if n <= 0:
        return triangle
    
    # Outer loop (rows of the triangle)
    for i in range(n):
        # initilize to 0 after each iteration
        current_row = []
        
        # inner loop (each element in current row)
        for j in range(i + 1):
            # checks if j is 0 or i is first or last element of the row and add 1)
            if j == 0 or j == i:
                current_row.append(1)
            else:
                current_row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        
        # add current row to the triangle
        triangle.append(current_row)
    
    return triangle

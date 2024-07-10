#!/usr/bin/python3
"""This script has a function that returns a list of lists of integers representing the Pascal’s triangle of n"""

def pascal_triangle(n):
	  # returns empty list if n is 0 or negative
    if n <= 0:
        return []

    # empty triangle array to store rows
    triangle = []
    
		#  generates pascal rows
    def generate_row(row_num):
			# base case (first row of triangle)
        if row_num == 0:
            return [1]
        else:
					# recursive call to obtain previous and current rows 
            prev_row = generate_row(row_num - 1)
						# adds [1] begin and end of row, middle part loops thru the prev row length and adds indices
            current_row = [1] + [prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)] + [1]
            return current_row
    
    for i in range(n):
			# adds each row to the triangle array
        triangle.append(generate_row(i))
    
    return triangle

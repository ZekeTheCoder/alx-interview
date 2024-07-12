#!/usr/bin/python3
"""
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """Function that calculates the fewest number of operations needed
                to result in exactly n H characters in the file.
                """

    number_of_operations = 0

    for divisor in range(2, n + 1):
        while n % divisor == 0:
            number_of_operations += divisor
            n /= divisor

    return number_of_operations

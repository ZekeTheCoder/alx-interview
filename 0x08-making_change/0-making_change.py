#!/usr/bin/python3
"""
0-making_change
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    Args:
        coins (list): A list of the values of the coins available.
        total (int): The total amount of money trying to make.
    Returns:
        int: The fewest number of coins needed to meet total, otherwise -1.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        num_current_coin = total // coin  # integer division
        num_coins += num_current_coin
        total -= num_current_coin * coin

        if total == 0:
            return num_coins

    return -1

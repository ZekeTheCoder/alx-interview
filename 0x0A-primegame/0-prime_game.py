#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):  # (n**0.5) square root of n
        if n % i == 0:
            return False
    return True


def get_primes(n):
    """Get all prime numbers up to n."""
    primes_list = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes_list.append(i)
    return primes_list  # list of primes


def count_primes_up_to(n, primes):
    """ Count the number of primes <= n. """
    count = 0
    for p in primes:
        if p <= n:
            count += 1
        else:
            break
    return count


def isWinner(x, nums):
    """ Determine the winner of the Prime Game. """
    if not nums or x < 1:
        return None

    max_n = max(nums)

    primes = get_primes(max_n)  # Cache primes

    # win counters
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Determine the number of primes up to n
        prime_count = count_primes_up_to(n, primes)
        # prime_count = sum(1 for p in primes if p <= n)

        if prime_count % 2 == 0:
            ben_wins += 1  # number of primes even
        else:
            maria_wins += 1  # number of primes odd

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

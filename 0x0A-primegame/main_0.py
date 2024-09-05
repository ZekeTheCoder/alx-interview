#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

# Test case 1: Original test
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

# Test case 2: Empty list
print("Test 2:", isWinner(3, []))

# Test case 3: All ones
print("Test 3:", isWinner(5, [1, 1, 1, 1, 1]))

# Test case 4: Large numbers
print("Test 4:", isWinner(10, [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]))

# Test case 5: Mixed small and large numbers
print("Test 5:", isWinner(7, [2, 4, 6, 8, 10, 100, 1000]))

# Test case 6: Equal wins
print("Test 6:", isWinner(4, [2, 3, 4, 5]))

# Test case 7: Single round
print("Test 7:", isWinner(1, [10]))

# Test case 8: Zero rounds
print("Test 8:", isWinner(0, [1, 2, 3]))

# Test case 9: Negative number in nums
print("Test 9:", isWinner(3, [-1, 2, 3]))

# Test case 10: Very large number of rounds
print("Test 10:", isWinner(10000, [i for i in range(1, 10001)]))
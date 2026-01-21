"""
File: comprehensions.py
Description:
    Shows list and dictionary comprehensions used for fast data processing.
Author: Saswati Barik
Level: Intermediate
"""

# 🔹 Example 1: List Comprehension
squares = [x * x for x in range(5)]
print("Squares:", squares)
# Expected Output:
# Squares: [0, 1, 4, 9, 16]

# 🔹 Example 2: Filter Even Numbers
evens = [x for x in range(10) if x % 2 == 0]
print("Evens:", evens)
# Expected Output:
# Evens: [0, 2, 4, 6, 8]

# 🔹 Example 3: Dictionary Comprehension
squareMap = {x: x * x for x in range(5)}
print("Square Map:", squareMap)
# Expected Output:
# Square Map: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

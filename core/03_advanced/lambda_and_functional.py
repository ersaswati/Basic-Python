"""
File: lambda_and_functional.py
Description:
    Demonstrates lambda functions and functional programming concepts.
Author: Saswati Barik
Level: Advanced
"""

# 🔹 Example 1: Lambda Function
square = lambda x: x * x
print("Lambda Output:", square(5))
# Expected Output:
# Lambda Output: 25

# 🔹 Example 2: map()
numbers = [1, 2, 3]
squaredNumbers = list(map(lambda x: x * x, numbers))
print("Map Output:", squaredNumbers)
# Expected Output:
# Map Output: [1, 4, 9]

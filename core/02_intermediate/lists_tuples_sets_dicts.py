"""
File: lists_tuples_sets_dicts.py
Description:
    Demonstrates core Python data structures used heavily in AI pipelines.
Author: Saswati Barik
Level: Intermediate
"""

# 🔹 Example 1: List (Ordered, Mutable)
numbers = [1, 2, 3]
numbers.append(4)
print("List:", numbers)
# Expected Output:
# List: [1, 2, 3, 4]

# 🔹 Example 2: Tuple (Ordered, Immutable)
coordinates = (10, 20)
print("Tuple:", coordinates)
# Expected Output:
# Tuple: (10, 20)

# 🔹 Example 3: Set (Unique, Unordered)
uniqueIds = {1, 2, 2, 3}
print("Set:", uniqueIds)
# Expected Output:
# Set: {1, 2, 3}

# 🔹 Example 4: Dictionary (Key-Value)
user = {"name": "Alice", "age": 30}
print("Dictionary:", user)
# Expected Output:
# Dictionary: {'name': 'Alice', 'age': 30}

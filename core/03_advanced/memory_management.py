"""
File: memory_management.py
Description:
    Demonstrates memory management concepts in Python.
Author: Saswati Barik
Level: Advanced
"""

import sys

# 🔹 Example 1: Object size in memory
numbers = [1, 2, 3, 4, 5]
print("Memory size:", sys.getsizeof(numbers))
# Expected Output:
# Memory size: (platform dependent)

# 🔹 Example 2: Generator vs List (Memory Efficient)
listData = [i for i in range(1000)]
generatorData = (i for i in range(1000))

print("List size:", sys.getsizeof(listData))
print("Generator size:", sys.getsizeof(generatorData))
# Expected Output:
# List size: larger than generator size

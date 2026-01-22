"""
File: decorators_and_generators.py
Description:
    Demonstrates decorators and generators used in performance optimization.
Author: Saswati Barik
Level: Advanced
"""

# 🔹 Example 1: Decorator
def log_execution(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")
    return wrapper

@log_execution
def process_data():
    print("Processing data")

process_data()
# Expected Output:
# Function started
# Processing data
# Function ended

# 🔹 Example 2: Generator
def number_generator(n):
    for i in range(n):
        yield i

print("Generator Output:", list(number_generator(3)))
# Expected Output:
# Generator Output: [0, 1, 2]

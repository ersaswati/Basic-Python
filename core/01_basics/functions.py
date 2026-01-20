"""
File: functions.py
Description:
    This script demonstrates how to define and use functions in Python.
Author: Saswati Barik
Level: Beginner
"""

def add_numbers(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: Sum of a and b
    """
    return a + b


# Function call
result = add_numbers(5, 3)

# Output the result
print("Sum:", result)

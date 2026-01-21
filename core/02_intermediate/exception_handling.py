"""
File: exception_handling.py
Description:
    Demonstrates error handling to build robust AI pipelines.
Author: Saswati Barik
Level: Intermediate
"""

# ⚠️ Example 1: Handling Division Error
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
# Expected Output:
# Error: division by zero

# 🔹 Example 2: Using finally
try:
    number = int("abc")
except ValueError:
    print("Invalid conversion")
finally:
    print("Execution completed")
# Expected Output:
# Invalid conversion
# Execution completed

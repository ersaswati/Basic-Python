"""
File: variables_and_datatypes.py
Description:
    This script demonstrates different types of variables and
    built-in data types in Python with examples and expected outputs.
Author: Saswati Barik
Level: Beginner (Level 1)
"""

# -----------------------------
# Example 1: String Variable
# -----------------------------
userName = "Alice"
print("User Name:", userName)
# Expected Output:
# User Name: Alice

# -----------------------------
# Example 2: Integer Variable
# -----------------------------
userAge = 28
print("User Age:", userAge)
# Expected Output:
# User Age: 28

# -----------------------------
# Example 3: Float Variable
# -----------------------------
userHeight = 5.6
print("User Height:", userHeight)
# Expected Output:
# User Height: 5.6

# -----------------------------
# Example 4: Boolean Variable
# -----------------------------
isStudent = True
print("Is Student:", isStudent)
# Expected Output:
# Is Student: True

# -----------------------------
# Example 5: Multiple Assignment
# -----------------------------
x, y, z = 10, 20, 30
print("x:", x, "y:", y, "z:", z)
# Expected Output:
# x: 10 y: 20 z: 30

# -----------------------------
# Example 6: Dynamic Typing
# -----------------------------
dataValue = 100
print("Data Value:", dataValue, "| Type:", type(dataValue))

dataValue = "Python"
print("Data Value:", dataValue, "| Type:", type(dataValue))
# Expected Output:
# Data Value: 100 | Type: <class 'int'>
# Data Value: Python | Type: <class 'str'>

# -----------------------------
# Example 7: Type Casting
# -----------------------------
stringNumber = "50"
convertedNumber = int(stringNumber)
print("Converted Number:", convertedNumber)
# Expected Output:
# Converted Number: 50

# -----------------------------
# Example 8: Arithmetic Operations
# -----------------------------
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
# Expected Output:
# Addition: 13
# Subtraction: 7
# Multiplication: 30
# Division: 3.3333333333333335

# -----------------------------
# Example 9: String + Number (Type Error Avoidance)
# -----------------------------
itemCount = 5
message = "Total items: " + str(itemCount)
print(message)
# Expected Output:
# Total items: 5

# -----------------------------
# Example 10: None Type
# -----------------------------
result = None
print("Result:", result)
print("Type of result:", type(result))
# Expected Output:
# Result: None
# Type of result: <class 'NoneType'>

# -----------------------------
# Example 11: Checking Variable Type
# -----------------------------
value = 3.14
print("Is float:", isinstance(value, float))
# Expected Output:
# Is float: True

# -----------------------------
# Example 12: Constant Convention
# -----------------------------
PI = 3.14159  # Constants are written in uppercase by convention
print("PI Value:", PI)
# Expected Output:
# PI Value: 3.14159

"""
File: file_handling.py
Description:
    Demonstrates basic file read/write operations.
Author: Saswati Barik
Level: Intermediate
"""

# 🔹 Example 1: Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello AI Engineer")

print("File written successfully")

# 🔹 Example 2: Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()

print("File Content:", content)
# Expected Output:
# File written successfully
# File Content: Hello AI Engineer

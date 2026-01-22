"""
File: context_managers.py
Description:
    Demonstrates context managers used for resource management.
Author: Saswati Barik
Level: Advanced
"""

# 🔹 Example: Using context manager
with open("context.txt", "w") as file:
    file.write("Context Manager Example")

print("Context manager executed")
# Expected Output:
# Context manager executed

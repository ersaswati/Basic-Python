"""
File: oop_basics.py
Description:
    Demonstrates Object-Oriented Programming concepts used in AI systems.
Author: Saswati Barik
Level: Advanced
"""

# 🔹 Example 1: Class and Object
class Model:
    def __init__(self, name):
        self.name = name

    def predict(self):
        return f"{self.name} is predicting"

model = Model("AI_Model")
print("OOP Output:", model.predict())
# Expected Output:
# OOP Output: AI_Model is predicting

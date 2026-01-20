"""
File: string_operations.py
Description:
    This script demonstrates commonly used string operations in Python.
    It also shows the expected output for each operation to help beginners
    understand how string methods work.
Author: Saswati Barik
Level: Beginner (Level 1)
"""

# Original string
text = "  Hello AI Engineer  "

# Convert string to uppercase
upperCaseText = text.upper()
print("Uppercase:", upperCaseText)
# Expected Output:
# Uppercase:   HELLO AI ENGINEER  

# Convert string to lowercase
lowerCaseText = text.lower()
print("Lowercase:", lowerCaseText)
# Expected Output:
# Lowercase:   hello ai engineer  

# Remove leading and trailing spaces
strippedText = text.strip()
print("Stripped:", strippedText)
# Expected Output:
# Stripped: Hello AI Engineer

# Replace a word in the string
replacedText = strippedText.replace("AI", "ML")
print("Replaced:", replacedText)
# Expected Output:
# Replaced: Hello ML Engineer

# Find the position of a substring
indexPosition = strippedText.find("Engineer")
print("Index of 'Engineer':", indexPosition)
# Expected Output:
# Index of 'Engineer': 9

# Check if string starts with a specific word
startsWithHello = strippedText.startswith("Hello")
print("Starts with 'Hello':", startsWithHello)
# Expected Output:
# Starts with 'Hello': True

# Check if string ends with a specific word
endsWithEngineer = strippedText.endswith("Engineer")
print("Ends with 'Engineer':", endsWithEngineer)
# Expected Output:
# Ends with 'Engineer': True

# Split string into a list of words
splitText = strippedText.split()
print("Split words:", splitText)
# Expected Output:
# Split words: ['Hello', 'AI', 'Engineer']

# Join list of words into a single string
joinedText = "-".join(splitText)
print("Joined text:", joinedText)
# Expected Output:
# Joined text: Hello-AI-Engineer

# Count occurrences of a character
countOfE = strippedText.count("e")
print("Count of 'e':", countOfE)
# Expected Output:
# Count of 'e': 3

# Check if string contains only alphabets (ignoring spaces)
isAlphaOnly = strippedText.replace(" ", "").isalpha()
print("Contains only alphabets:", isAlphaOnly)
# Expected Output:
# Contains only alphabets: True

# Check if string contains only digits
digitText = "12345"
isDigitOnly = digitText.isdigit()
print("Contains only digits:", isDigitOnly)
# Expected Output:
# Contains only digits: True

# Capitalize the first letter of the string
capitalizedText = strippedText.capitalize()
print("Capitalized:", capitalizedText)
# Expected Output:
# Capitalized: Hello ai engineer

# Title case conversion
titleCaseText = strippedText.title()
print("Title Case:", titleCaseText)
# Expected Output:
# Title Case: Hello Ai Engineer

# Swap case (uppercase <-> lowercase)
swappedCaseText = strippedText.swapcase()
print("Swapped Case:", swappedCaseText)
# Expected Output:
# Swapped Case: hELLO ai eNGINEER

# Length of string
stringLength = len(strippedText)
print("Length:", stringLength)
# Expected Output:
# Length: 17

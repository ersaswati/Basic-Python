"""
File: tricky_python_questions.py
Description:
    This script contains commonly asked tricky Python interview questions.
    Each example includes explanation and expected output.
    These questions test understanding of mutability, memory,
    object references, and Python internals.
Author: Saswati Barik
Level: Interview (Beginner → Advanced)
"""

# --------------------------------------------------
# 🔹Example 1: Immutable Integer Behavior
# --------------------------------------------------
x = 10
y = x
y = 20

print("Example 1 Output:", x)
# Expected Output:
# 🔍Example 1 Output: 10

# Explanation:
# Integers are immutable. Reassigning y creates a new object.

# --------------------------------------------------
# 🔹Example 2: Mutable List Behavior
# --------------------------------------------------
a = [1, 2, 3]
b = a
b.append(4)

print("Example 2 Output:", a)
# Expected Output:
# 🔍Example 2 Output: [1, 2, 3, 4]

# Explanation:
# Lists are mutable. Both variables refer to the same list.

# --------------------------------------------------
# 🔹Example 3: Default Mutable Argument (Trick Question)
# --------------------------------------------------
def add_item(item, items=[]):
    items.append(item)
    return items

print("Example 3 Output 1:", add_item(1))
print("Example 3 Output 2:", add_item(2))
# Expected Output:
# 🔍Example 3 Output 1: [1]
# 🔍Example 3 Output 2: [1, 2]

# Explanation:
# Default arguments are evaluated only once.

# --------------------------------------------------
# 🔹Example 4: Correct Way to Handle Default Arguments
# --------------------------------------------------
def safe_add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print("Example 4 Output:", safe_add_item(1))
# Expected Output:
# 🔍Example 4 Output: [1]

# --------------------------------------------------
# 🔹Example 5: == vs is
# --------------------------------------------------
print("Example 5 Output 1:", [] == [])
print("Example 5 Output 2:", [] is [])
# Expected Output:
# 🔍Example 5 Output 1: True
# 🔍Example 5 Output 2: False

# Explanation:
# == checks value equality, is checks memory reference.

# --------------------------------------------------
# 🔹Example 6: String Immutability
# --------------------------------------------------
text = "python"

try:
    text[0] = "P"
except TypeError as e:
    print("Example 6 Output:", e)
# Expected Output:
# 🔍Example 6 Output: 'str' object does not support item assignment

# --------------------------------------------------
# 🔹Example 7: Loop Variable Scope
# --------------------------------------------------
for i in range(3):
    pass

print("Example 7 Output:", i)
# Expected Output:
# 🔍Example 7 Output: 2

# Explanation:
# Python does not have block-level scope for loops.

# --------------------------------------------------
# 🔹Example 8: None in Conditional
# --------------------------------------------------
if None:
    print("Yes")
else:
    print("Example 8 Output: No")
# Expected Output:
# 🔍Example 8 Output: No

# --------------------------------------------------
# 🔹Example 9: Boolean of Non-empty String
# --------------------------------------------------
print("Example 9 Output:", bool("False"))
# Expected Output:
# 🔍Example 9 Output: True

# Explanation:
# Any non-empty string evaluates to True.

# --------------------------------------------------
# 🔹Example 10: += vs +
# --------------------------------------------------
a = [1, 2]
b = a
a += [3]

print("Example 10 Output:", b)
# Expected Output:
# 🔍Example 10 Output: [1, 2, 3]

# --------------------------------------------------
# 🔹Example 11: Integer Caching
# --------------------------------------------------
a = 256
b = 256
c = 257
d = 257

print("Example 11 Output 1:", a is b)
print("Example 11 Output 2:", c is d)
# Expected Output:
# 🔍Example 11 Output 1: True
# 🔍Example 11 Output 2: False

# --------------------------------------------------
# 🔹Example 12: Floating Point Precision
# --------------------------------------------------
print("Example 12 Output:", 0.1 + 0.2 == 0.3)
# Expected Output:
# 🔍Example 12 Output: False

'''
✅ Correct Way to Compare Floating-Point Numbers
1) print(round(0.1 + 0.2, 2) == 0.3)
2) Using math.isclose() (Best Practice)
    import math
    print(math.isclose(0.1 + 0.2, 0.3))
'''

# --------------------------------------------------
# 🔹Example 13: Function Return Value
# --------------------------------------------------
def greet():
    print("Hello")

print("Example 13 Output:", greet())
# Expected Output:
# Hello
# 🔍Example 13 Output: None

# --------------------------------------------------
# 🔹Example 14: Dictionary with Tuple Key
# --------------------------------------------------
data = {(1, 2): "value"}
print("Example 14 Output:", data[(1, 2)])
# Expected Output:
# 🔍Example 14 Output: value

# --------------------------------------------------
# 🔹Example 15: List as Dictionary Key (Error)
# --------------------------------------------------
try:
    invalidDict = {[1, 2]: "value"}
except TypeError as e:
    print("Example 15 Output:", e)
# Expected Output:
# 🔍Example 15 Output: unhashable type: 'list'

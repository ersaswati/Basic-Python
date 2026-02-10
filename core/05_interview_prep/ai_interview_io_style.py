"""
PROBLEM 1: Most Frequent Element

Input:
nums = [1, 2, 2, 3, 3, 3, 4]

Output:
3

Write a function that returns the most frequent element.
"""

def most_frequent(nums):
    # WRITE LOGIC HERE
    from collections import Counter
    return Counter(nums).most_common(1)[0][0]


# Test
print(most_frequent([1, 2, 2, 3, 3, 3, 4]))



"""
PROBLEM 2: Flatten Nested List

Input:
lst = [1, [2, [3, 4]], 5]

Output:
[1, 2, 3, 4, 5]
"""

def flatten(lst):
    # WRITE LOGIC HERE
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, 4]], 5]))



"""
PROBLEM 3: Two Sum

Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]
"""

def two_sum(nums, target):
    # WRITE LOGIC HERE
    lookup = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in lookup:
            return [lookup[diff], i]
        lookup[num] = i

print(two_sum([2, 7, 11, 15], 9))



"""
PROBLEM 4: Remove Duplicates but Keep Order

Input:
[1, 2, 2, 3, 1, 4]

Output:
[1, 2, 3, 4]
"""

def remove_duplicates(lst):
    # WRITE LOGIC HERE
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4]))



"""
PROBLEM 5: Binary Search

Input:
arr = [1, 3, 5, 7, 9]
target = 5

Output:
2
"""

def binary_search(arr, target):
    # WRITE LOGIC HERE
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9], 5))



"""
PROBLEM 6: Normalize NumPy Array

Input:
[10, 20, 30]

Output:
Array with mean=0 and std=1
"""

import numpy as np

def normalize(x):
    # WRITE LOGIC HERE
    return (x - x.mean()) / x.std()

print(normalize(np.array([10, 20, 30])))



"""
PROBLEM 7: Batch Generator

Input:
data = [0,1,2,3,4,5,6,7,8,9]
batch_size = 3

Output:
[0,1,2]
[3,4,5]
[6,7,8]
[9]
"""

def batch_generator(data, batch_size):
    # WRITE LOGIC HERE
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]

for batch in batch_generator(list(range(10)), 3):
    print(batch)



"""
PROBLEM 8: Fix Mutable Default Argument Bug

Input:
Call function multiple times

Output:
Should NOT keep old values
"""

def add_item(item, lst=None):
    # WRITE LOGIC HERE
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))
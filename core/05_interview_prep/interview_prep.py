"""
Q1: Find the most frequent element in a list.
"""

from collections import Counter

def most_frequent(nums):
    return Counter(nums).most_common(1)[0][0]

print("Most frequent:", most_frequent([1, 2, 2, 3, 3, 3, 4]))


"""
Q2: Flatten a nested list of any depth.
Example: [1, [2, [3, 4]], 5] → [1, 2, 3, 4, 5]
"""

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print("Flattened:", flatten([1, [2, [3, 4]], 5]))


"""
Q3: Remove duplicates from a list but keep original order.
"""

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print("No duplicates:", remove_duplicates([1, 2, 2, 3, 1, 4]))


"""
Q4: Two Sum — return indices of two numbers that add up to target.
"""

def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in lookup:
            return [lookup[diff], i]
        lookup[num] = i

print("Two Sum:", two_sum([2, 7, 11, 15], 9))


"""
Q5: Binary Search — find index of target in sorted array.
"""

def binary_search(arr, target):
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

print("Binary Search:", binary_search([1, 3, 5, 7, 9], 5))


"""
Q6: Reverse a singly linked list.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


"""
Q7: Normalize a NumPy array (mean=0, std=1).
"""

import numpy as np

def normalize(x):
    return (x - x.mean()) / x.std()

arr = np.array([10, 20, 30])
print("Normalized:", normalize(arr))


"""
Q8: Create a batch generator for ML training.
"""

def batch_generator(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]

print("Batches:")
for batch in batch_generator(list(range(10)), 3):
    print(batch)


"""
Q9: Explain and fix the mutable default argument problem.
"""

def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print("Mutable fix:", add_item(1))
print("Mutable fix:", add_item(2))


"""
Q10: Compare Python loop vs NumPy vectorization performance.
"""

import time

arr = np.arange(1_000_000)

start = time.time()
result = [i*i for i in range(1_000_000)]
print("List comprehension time:", time.time() - start)

start = time.time()
result = arr ** 2
print("NumPy vectorized time:", time.time() - start)
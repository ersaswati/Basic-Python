"""
PROBLEM 1: Most Frequent Element

Input:
[1, 2, 2, 3, 3, 3, 4]

Output:
3
"""

def most_frequent(nums):
    max_count = 0
    result = None

    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1

        if count > max_count:
            max_count = count
            result = nums[i]

    return result

print(most_frequent([1, 2, 2, 3, 3, 3, 4]))

"""
PROBLEM 2: Remove Duplicates (Keep Order)

Input:
[1, 2, 2, 3, 1, 4]

Output:
[1, 2, 3, 4]
"""

def remove_duplicates(lst):
    result = []

    for item in lst:
        exists = False
        for r in result:
            if r == item:
                exists = True
                break

        if not exists:
            result.append(item)

    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4]))


"""
PROBLEM 3: Two Sum

Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]
"""

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(two_sum([2, 7, 11, 15], 9))


"""
PROBLEM 4: Binary Search

Input:
[1, 3, 5, 7, 9], target=5

Output:
2
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

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
PROBLEM 5: Flatten Nested List (No libraries)

Input:
[1, [2, [3, 4]], 5]

Output:
[1, 2, 3, 4, 5]
"""

def flatten(lst):
    result = []

    for item in lst:
        if type(item) == list:
            inner = flatten(item)
            for val in inner:
                result.append(val)
        else:
            result.append(item)

    return result

print(flatten([1, [2, [3, 4]], 5]))

"""
PROBLEM 6: Normalize List (No NumPy)

Input:
[10, 20, 30]

Output:
Normalized list
"""

def normalize(arr):
    total = 0
    for x in arr:
        total += x

    mean = total / len(arr)

    var_sum = 0
    for x in arr:
        var_sum += (x - mean) ** 2

    std = (var_sum / len(arr)) ** 0.5

    result = []
    for x in arr:
        result.append((x - mean) / std)

    return result

print(normalize([10, 20, 30]))

"""
PROBLEM 7: Batch Generator (Basic Logic)

Input:
data = [0,1,2,3,4,5,6,7,8,9]
batch_size = 3
"""

def batch_generator(data, batch_size):
    i = 0
    while i < len(data):
        batch = []
        j = i
        while j < i + batch_size and j < len(data):
            batch.append(data[j])
            j += 1

        yield batch
        i += batch_size

for b in batch_generator(list(range(10)), 3):
    print(b)


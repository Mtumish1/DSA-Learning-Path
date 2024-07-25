"""Description:
Write a function that finds and returns the maximum element in an array of integers.

Example:
    Input: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    Output: 9

Why It's Important:
Finding the maximum element is a basic problem that helps with understanding array traversal and comparison operations. It is a fundamental concept used in various algorithms and data manipulation tasks.
"""


# Python Example Solution:

def find_maximum(arr: list[int]) -> int:
    if not arr:
        raise ValueError("Array is empty")
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

# Example usage

print(find_maximum([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  # Output: 9

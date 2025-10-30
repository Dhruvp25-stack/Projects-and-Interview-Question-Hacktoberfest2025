"""
Author: Dhruv Patni
Repository: Projects-and-Interview-Question-Hacktoberfest2025
File: top_dsa_patterns.py

Description:
-------------
This script contains implementations of common Data Structures & Algorithm (DSA)
patterns frequently asked in coding interviews. Each function is optimized for
clarity and understanding.
"""

# -----------------------------
# 1️⃣ Sliding Window Example
# -----------------------------
def max_subarray_sum(nums, k):
    """
    Find the maximum sum of any subarray of size k.
    Example: nums = [2, 1, 5, 1, 3, 2], k = 3 → output = 9
    """
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


# -----------------------------
# 2️⃣ Two Pointer Technique
# -----------------------------
def two_sum_sorted(arr, target):
    """
    Find two numbers in a sorted array that sum to a target.
    Example: arr = [1, 2, 3, 4, 6], target = 6 → output = (1, 3)
    """
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None


# -----------------------------
# 3️⃣ Hash Map Pattern
# -----------------------------
def first_non_repeating_char(s):
    """
    Return the first non-repeating character in a string.
    Example: s = "swiss" → output = 'w'
    """
    char_count = {}
    for ch in s:
        char_count[ch] = char_count.get(ch, 0) + 1

    for ch in s:
        if char_count[ch] == 1:
            return ch
    return None


# -----------------------------
# 4️⃣ Binary Search
# -----------------------------
def binary_search(arr, key):
    """
    Perform binary search on a sorted array.
    Example: arr = [1, 3, 5, 7, 9], key = 5 → output = 2
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# -----------------------------
# 5️⃣ Recursion (Factorial)
# -----------------------------
def factorial(n):
    """
    Recursive factorial example.
    Example: factorial(5) → 120
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# -----------------------------
# 🔍 Demo Section
# -----------------------------
if __name__ == "__main__":
    print("1️⃣ Max Subarray Sum:", max_subarray_sum([2, 1, 5, 1, 3, 2], 3))
    print("2️⃣ Two Sum Sorted:", two_sum_sorted([1, 2, 3, 4, 6], 6))
    print("3️⃣ First Non-Repeating Char:", first_non_repeating_char("swiss"))
    print("4️⃣ Binary Search (index):", binary_search([1, 3, 5, 7, 9], 5))
    print("5️⃣ Factorial of 5:", factorial(5))

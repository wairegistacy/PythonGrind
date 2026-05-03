# SEARCH ALGORITHM
# TWO TYPES:
# 1. Linear Search Algorithm: Time complexity: 0(n), Space Complexity: 0(1)
def get_element(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1

# 2. Binary Search Algorithm: Time Complexity: 0(log n), Space Complexity: 0(1)
def get_element(arr, target):
    n = len(arr)
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# QUESTIONS: Leetcode
# QUESTION 1: Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.You must write an algorithm with O(log n) runtime complexity.
def get_element(arr, target):
    n = len(arr)
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# QUESTION 2: Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.
def get_element(arr, target):
    n = len(arr)
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start
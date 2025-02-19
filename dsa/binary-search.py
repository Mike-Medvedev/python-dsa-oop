# Basic binary search implementation in python

def binary_search(arr, target):
    """Performs a binary search on a sorted array"""
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        elif guess < target:
            low = mid + 1
    return None


sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_num = 11

print(binary_search(sorted_arr, target_num))

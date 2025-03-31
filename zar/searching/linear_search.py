def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
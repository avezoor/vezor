def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print(f"Element {target} found at index {mid}.")
            return
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(f"Element {target} not found in the array.")
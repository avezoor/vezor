def ordered_linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            print(f"Element {target} found at index {index}.")
            return
        elif element > target:
            break
    print(f"Element {target} not found in the array.")
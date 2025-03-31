def min_distance(arr):
    arr.sort()
    min_diff = float('inf')
    closest_pair = ()

    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (arr[i], arr[i + 1])

    print(f"Minimum distance is {min_diff}")
    print(f"Closest pair is {closest_pair}")
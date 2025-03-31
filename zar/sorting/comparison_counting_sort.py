def comparison_counting_sort(arr):
    n = len(arr)
    sorted_arr = [0] * n

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] < arr[i] or (arr[j] == arr[i] and j < i):
                count += 1
        sorted_arr[count] = arr[i]

    return sorted_arr
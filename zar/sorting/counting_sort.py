def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, range_of_elements):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]
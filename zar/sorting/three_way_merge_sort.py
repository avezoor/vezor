def __merge_three(left, middle, right):
    result = []
    i = j = k = 0

    while i < len(left) or j < len(middle) or k < len(right):
        values = []
        if i < len(left):
            values.append((left[i], 'l'))
        if j < len(middle):
            values.append((middle[j], 'm'))
        if k < len(right):
            values.append((right[k], 'r'))

        values.sort()
        val, source = values[0]

        if source == 'l':
            i += 1
        elif source == 'm':
            j += 1
        else:
            k += 1

        result.append(val)

    return result

def three_way_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    third = len(arr) // 3
    if third == 0:  
        return sorted(arr)  

    left = three_way_merge_sort(arr[:third])
    middle = three_way_merge_sort(arr[third:2 * third])
    right = three_way_merge_sort(arr[2 * third:])

    return __merge_three(left, middle, right)
def find_indexes(arr, min_val, max_val):
    indexes = []
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            indexes.append(i)
    return indexes
    
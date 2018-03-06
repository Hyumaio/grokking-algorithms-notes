def find_smallest(arr):
    """Find the smallest element in an array."""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    """Sort an array from smallest to largest."""
    new_arr = list()
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        # Get smallest by smallest_index, remove it from the old array, then append it to the new array.
        new_arr.append(arr.pop(smallest_index))
    return new_arr


if __name__ == '__main__':
    ARR = [43, 21, 24, 35, 81, 4, 27, 78, 71, 46, 31, 9]
    NEW_ARR = selection_sort(ARR)
    print('After selection sort, the new array is', NEW_ARR)

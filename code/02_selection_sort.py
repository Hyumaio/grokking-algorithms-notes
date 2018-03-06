def findSmallest(arr):
    """Find the smallest element in an array."""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    """Sort an array from smallest to largest."""
    newArr = list()
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        # Get smallest by smallest_index, remove it from the old array, then append it to the new array.
        newArr.append(arr.pop(smallest_index))
    return newArr


if __name__ == '__main__':
    arr = [43, 21, 24, 35, 81, 4, 27, 78, 71, 46, 31, 9]
    newArr = selectionSort(arr)
    print('After selection sort, the new array is', newArr)

import copy


def sum_recursion(arr):
    """Use D&C to sum an array."""
    if not arr:
        # The base case
        return 0
    # The recursive case
    return arr.pop(0) + sum_recursion(arr)


def sum_loop(arr):
    """Use loop to sum an array"""
    total = 0
    for i in arr:
        total += i
    return total


if __name__ == '__main__':
    ARR = [x for x in range(2, 12, 2)]
    RESULT = sum_recursion(copy.copy(ARR))
    print('D&C sum', RESULT)
    print('Loop sum:', sum_loop(ARR))

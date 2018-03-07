import random


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # Use random pivot everytime can avoid the worst case.
    pivot = arr[random.randrange(len(arr))]
    return quick_sort([lt for lt in arr if lt < pivot]) + [pivot] + quick_sort([rt for rt in arr if rt > pivot])


if __name__ == '__main__':
    ARR = [14, 26, 24, 42, 1, 34, 54, 33, 11]
    # RESULT = bubble_sort(ARR)  # O(n**2)
    RESULT = quick_sort(ARR)  # O(n*log n) if not the worst case else O(n**2)
    print(RESULT)

    # # Operation time test
    # # 1.Operation time of bubble_sort
    # ARR2 = [x for x in range(10000)]
    # start = time()
    # RESULT2 = bubble_sort(ARR2)  # Output seems around 6s in my PC
    # print('Operation time of bubble_sort:', time() - start)
    # # 2.Operation time of quick_sort
    # start = time()
    # RESULT2 = quick_sort(ARR2)  # Output seems around 0.04s in my PC
    # print('Operation time of quick_sort:', time() - start)

def binary_search(lst, element):
    """Binary search."""
    low_index = 0
    high_index = len(lst) - 1

    # While the given element hasn't been found yet.
    times = 0
    while low_index <= high_index:
        times += 1
        mid_index = (low_index + high_index) // 2
        guess = lst[mid_index]
        if guess == element:
            return mid_index, times
        if guess > element:
            high_index = mid_index - 1
        else:
            # guess < element
            low_index = mid_index + 1

    # When element doesn't exist.
    return None, None


def simple_search(lst, element):
    """Simple search."""
    times = 0
    for i in lst:
        times += 1
        if i == element:
            element_index = lst.index(i)
            return element_index, times
    return None, None


if __name__ == '__main__':
    ELEMENT = 240000
    LST = [x for x in range(1, 240000 + 1)]

    # 1.Simple search
    # ELEMENT_INDEX, TIMES = simple_search(LST, ELEMENT)

    # 2.Binary search
    ELEMENT_INDEX, TIMES = binary_search(LST, ELEMENT)

    if ELEMENT_INDEX is None:
        print('Cannot find %s in the given list.' % ELEMENT)
    else:
        print("Element(%s)'s index is %s, used %s times to search out." % (ELEMENT, ELEMENT_INDEX, TIMES))

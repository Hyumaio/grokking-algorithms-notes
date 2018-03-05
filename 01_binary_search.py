def binarySearch(lst, element):
    """Binary search."""
    assert isinstance(lst, list), "'lst' must be a list object."
    low_index = 0
    high_index = len(lst) - 1

    # While the given element hasn't been found yet.
    times = 1
    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2
        guess = lst[mid_index]
        if guess == element:
            return mid_index, times
        if guess > element:
            high_index = mid_index - 1
        else:
            # guess < element
            low_index = mid_index + 1
        times += 1

    # When element doesn't exist.
    return None, None


def search(lst, element):
    """Simple search."""
    times = 1
    for i in lst:
        if i == element:
            element_index = lst.index(i)
            return element_index, times
        times += 1
    return None, None


element = 240000
lst = [x for x in range(1, 240000 + 1)]

# element_index, times = search(lst, element)
element_index, times = binarySearch(lst, element)

if element_index is None:
    print('Cannot find %s in the given list.' % element)
else:
    print("Element(%s)'s index is %s, used %s times to get." % (element, element_index, times))

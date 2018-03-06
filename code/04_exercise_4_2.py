import copy


def calculate_amount_recursion(lst):
    """Use recursion to calculate the amount of an array."""
    if not lst:
        # the base case
        return 0
    # the recursive case
    lst.pop()
    return 1 + calculate_amount_recursion(lst)


def calculate_amount_loop(lst):
    """Use loop to calculate the amount of an array."""
    amount = 0
    for i in range(len(lst)):
        amount += 1
    return amount


if __name__ == '__main__':
    LST = [x for x in range(326)]
    AMOUNT = calculate_amount_recursion(copy.copy(LST))
    print('Recursion amount:', AMOUNT)
    print('Loop amount:', calculate_amount_loop(LST))

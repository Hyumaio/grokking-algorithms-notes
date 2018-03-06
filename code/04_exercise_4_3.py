def max(lst):
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    sub_max = max(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max


if __name__ == '__main__':
    LST = [x for x in range(2, 12, 2)]
    MAX = max(LST)
    print(MAX)

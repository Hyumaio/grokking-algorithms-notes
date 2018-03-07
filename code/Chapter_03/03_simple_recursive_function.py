def factorial(number):
    """A simple realization of the factorial uses recursion."""
    if number == 1:
        return 1
    return number * factorial(number - 1)


if __name__ == '__main__':
    RESULT = factorial(5)
    print(RESULT)

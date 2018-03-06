"""
Euclidean Algorithm, also called Euclid's Algorithm, is a algorithm to solve the GCD(Greatest Common Divisor)/HCF(Highest Common Factor) of two numbers.
"""


def euclideanAlgorithm(numbers):
    foo, bar = numbers
    while True:
        remainder = foo % bar
        if remainder == 0:
            return bar
        else:
            foo, bar = bar, remainder


if __name__ == '__main__':
    numbers = (2000, 96)
    gcd = euclideanAlgorithm(numbers)
    print(gcd)

# =========================================================================================
# To get the GCD, there're two more solutions, I made a simple brief explanation down here.
#
# numbers = (2000, 96)
# =============================
# 1.Prime factor decomposition.
# 8|2000  96
# 2|250   12
#   125   6
#
# Result: 125 and 6 is relatively prime, so the GCD of (2000, 96) is 8*2=16.
# ==========================================================================
# 2.Short division.
# 2000 = 2*2*2*2*5*5*5
# 96   = 2*2*2*2*2*3
#
# Result: The common part after equal sign is the GCD of (2000, 96), so its 2*2*2*2=16.
# =====================================================================================

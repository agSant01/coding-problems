"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import math


def largest_prime_factor(number: int) -> int:
    factors = []
    top_ = math.ceil(math.sqrt(number))

    for i in range(2, top_):
        if number % i == 0:
            factors.append(i)

    largest_pf = None
    for factor in factors:
        isP = True
        for i in range(2, math.ceil(factor ** 0.5)):
            if factor % i == 0:
                isP = False
                break
        if isP:
            largest_pf = factor

    return largest_pf


print('Result =>', largest_prime_factor(13195))
assert largest_prime_factor(13195) == 29
print('Result =>', largest_prime_factor(600851475143))

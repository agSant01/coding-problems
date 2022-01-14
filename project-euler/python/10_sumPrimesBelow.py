"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


import math


def sum_prime_below(n: int) -> int:
    primes = [2]

    cnt = 1
    i = 3

    while i < n:
        isp = True
        sqrt_ = math.sqrt(i)

        for prime in primes:
            if prime > sqrt_:
                break

            if i % prime == 0:
                isp = False
                break

        if isp:
            cnt += 1
            primes.append(i)

        i += 2

    return sum(primes)


assert sum_prime_below(10) == 17
print('Result =>', sum_prime_below(2_000_000))

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import math


def nth_prime(n: int) -> int:
    primes = [2]

    cnt = 1
    i = 3

    while cnt < n:
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

    return primes[-1]


assert nth_prime(6) == 13

print('Result =>', nth_prime(10001))

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

        a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
"""
from math import sqrt


def pyt_triplet(n: int) -> int:
    for c in range(n+1):
        for b in range(c):
            if b+c > n:
                break
            for a in range(b):
                if a+b+c > n:
                    break
                if a**2 + b**2 == c**2:
                    if a+b+c == n:
                        return a*b*c
    return -1


r = pyt_triplet(3+4+5)
assert r == 3*4*5


print('Result =>', pyt_triplet(1000))

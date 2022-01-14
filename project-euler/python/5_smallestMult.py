"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import operator
import functools


def smallest_div(a, b):
    k = b
    while True:
        d = True

        for i in range(a, b+1):
            if k % i != 0:
                d = False
                break
        if d:
            return k

        k += b


assert smallest_div(1, 10) == 2520

print("Result =>", smallest_div(1, 20))

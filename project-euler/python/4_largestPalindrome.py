"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math


def is_palindrome(a: int) -> bool:
    a_ = str(a)

    lp = 0
    rp = len(a_) - 1

    while lp < rp:
        if a_[lp] != a_[rp]:
            return False
        lp += 1
        rp -= 1

    return True


assert is_palindrome(9009) == True
assert is_palindrome(9000) == False
assert is_palindrome(12321) == True


def largest_palindrome(power) -> int:
    max_ = -1

    for a in range(10**(power-1), 10**power):
        for b in range(10**(power-1), 10**power):
            c = a * b
            if c > max_ and is_palindrome(c):
                max_ = c

    return max_


assert largest_palindrome(2) == 9009

print('Result =>', largest_palindrome(3))

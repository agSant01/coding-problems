"""
The sum of the squares of the first ten natural numbers is,
    
       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def square_of_sum(n: int) -> int:
    return (n*(n+1)//2)**2


def sum_of_squares(n: int) -> int:
    s = 0
    for i in range(1, n+1):
        s += i**2
    return s


assert square_of_sum(10) == 3025

square = square_of_sum(100)
print(square)

assert sum_of_squares(10) == 385

sum_ = sum_of_squares(100)
print(sum_)

print('result => ', square-sum_)

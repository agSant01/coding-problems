from math import ceil, floor
from typing import List

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 83, 89, 101, 107, 113,
          131, 137, 149, 167, 173, 179, 191, 197, 227, 233, 239, 251, 257, 263]


def divisors(n: int) -> int:
    divs = 1
    for p in primes:
        cnt = 0
        while floor(n / p) == n / p:
            if n//p == 0:
                break
            n //= p
            cnt += 1

        divs *= cnt+1

        if p > n:
            break

    return divs


print(divisors(21))  # 4
print(divisors(28))  # 4
print(divisors(36))  # 9
print(divisors(360))  # 24

acc = 1
i = 2
while True:
    divs_ = divisors(acc)
    if divs_ >= 500:
        print(divs_, i, acc)  # 576 12376 76576500
        break

    acc += i
    i += 1

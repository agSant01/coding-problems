import math


def jumpingOnClouds(c, i=0):
    # Write your code here
    if len(c) == 0:
        return i-1

    if c[0] == 1:
        return math.inf

    j1 = jumpingOnClouds(c[1:], i+1)

    j2 = math.inf
    if len(c) > 2:
        j2 = jumpingOnClouds(c[2:], i+1)

    print(len(c), j1, j2)

    return min(j1, j2)


c = [0, 1, 0, 0, 0, 1, 0]
r = jumpingOnClouds(c)
print(r)
print('-'*10)
c = [0, 0, 1, 0, 0, 1, 0]
r = jumpingOnClouds(c)
print(r)
print('-'*10)

c = [0, 0, 0, 1, 0, 0]
r = jumpingOnClouds(c)
print(r)
print('-'*10)

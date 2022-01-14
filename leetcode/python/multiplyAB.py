def multiply(a: int, b: int):
    if a == 0 or b == 0:
        return 0

    if b == 1:
        return a

    if a == 1:
        return b

    if b < 0:
        a *= -1

    return a + multiply(a, abs(b)-1)


print((-2, 3), multiply(-2, 3))
print((0, 0), multiply(0, 0))
print((1, 3), multiply(1, 3))
print((3, -3), multiply(3, -3))
print((-2, -1), multiply(-2, -1))

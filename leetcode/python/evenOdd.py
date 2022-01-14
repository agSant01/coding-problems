def isEven(number: int):
    return bool(number % 2)


def isEvenBit(number: int):
    return number & 1


print(isEven(3))
print(isEven(4))

print(isEvenBit(3))
print(isEvenBit(4))

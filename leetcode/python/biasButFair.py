from random import randint

HEADS, TAILS = 1, 0


def biased():
    """
    HEADS with 20% probability
    A biased function that returns TAILS with 80% probability and

    Returns:
        Int: 1 if HEADS, 0 if TAILS
    """

    # generate a random number between 0–99, both inclusive
    r = randint(0, 99)

    # return TAILS if we got a number between [0–79]; otherwise, return HEADS
    return TAILS if (r <= 79) else HEADS


# Return HEADS and TAILS with equal probability using the specified function
def generate():
    while True:
        first = biased()
        second = biased()
        if first is not second:
            return first    # or return second


if __name__ == '__main__':
    x = y = 0
    bx = by = 0
    for i in range(100000):
        val = generate()
        print(val)
        if val > 0:
            x += 1
        else:
            y += 1

        bval = biased()
        if bval > 0:
            bx += 1
        else:
            by += 1

    print('HEADS ~', x / 1000, '%')        # ~50%
    print('TAILS ~', y / 1000, '%')        # ~50%
    print()
    print('B_HEADS ~', bx / 1000, '%')
    print('B_TAILS ~', by / 1000, '%')

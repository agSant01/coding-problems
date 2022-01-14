def print_n(n: int):
    if n < 1:
        return
    print_n(n-1)
    print(n)


print_n(4)

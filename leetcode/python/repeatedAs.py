
def repeatedString(s, n):
    # Write your code here
    sub_total = s.count('a')

    len_s = len(s)

    fits_inside = n // len_s
    remainder = n % len_s

    remainder_count = 0
    for c in s[:remainder]:
        remainder_count += (c == 'a')

    return (fits_inside * sub_total) + remainder_count


r = repeatedString('aba', 10)
print(r)

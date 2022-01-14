import queue
from typing import List


def combinationSum4(nums: List[int], target: int) -> int:
    combs = []

    q = queue.Queue()
    for num in nums:
        q.put((num, [num]))

    while not q.empty():
        curr, comb = q.get()

        if curr == target:
            combs.append(comb)
            continue

        for num in nums:
            if (num + curr) == target:
                combs.append(comb + [num])
            elif (num + curr) < target:
                q.put((curr+num, comb + [num]))

    return len(combs)


COMB = None


def helper(nums: List[int], target: int) -> int:
    global COMB

    if COMB[target] != 0:
        return COMB[target]

    c = 0
    for num in nums:
        if target >= num:
            c += helper(nums, target-num)

    COMB[target] = c

    return c


def comb_sum(nums: List[int], target: int) -> int:
    global COMB
    COMB = [0 for _ in range(target+1)]
    COMB[0] = 1
    return helper(nums, target)


def cs(nums: List[int], target: int) -> int:
    combs = [0 for _ in range(target+1)]
    combs[0] = 1

    for i in range(len(combs)):
        for num in nums:
            if (i - num) >= 0:
                combs[i] += combs[i - num]

    return combs[target]


l = [1, 2, 3]
t = 4
r = combinationSum4(l, t)
print('Result 1 ->', r, cs(l, t))

l = [9]
t = 3
r = combinationSum4(l, t)
print('Result 2 ->', r, cs(l, t))

l = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
     15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
t = 10
r = combinationSum4(l, t)
print('Result 3 ->', r, cs(l, t))


l = [4, 2, 1]
t = 32
r = comb_sum(l, t)
print('Result 4 ->', r)
print('Result 4.1 ->', cs(l, t))

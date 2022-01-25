from typing import List


def maxWidthOfVerticalArea(points: List[List[int]]) -> int:
    s = set()
    for x, _ in points:
        s.add(x)

    mw = 0
    sp = sorted(s)
    for i in range(len(sp)-1):
        w = sp[i+1] - sp[i]
        mw = max(w, mw)

    return mw


assert maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]) == 1
assert maxWidthOfVerticalArea(
    [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]) == 3

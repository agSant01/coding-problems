from typing import List

import collections


def longestCommonPrefix(strs: List[str]) -> str:
    a = collections.defaultdict(int)
    for i1, s in enumerate(strs):
        for i2, c in enumerate(s):
            a[c] += 1
            if a[c] != i1+1:
                return s[:i2]
    return ''


assert longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
assert longestCommonPrefix(["dog", "racecar", "car"]) == ''
assert longestCommonPrefix(["dog", "dogger", "doggy"]) == 'dog'

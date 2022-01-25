import collections
import argparse


class TimeMapTuple:
    def __init__(self):
        self.h = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        res = self.h.get((key, timestamp))
        while res is None and timestamp > 0:
            timestamp -= 1
            res = self.h.get((key, timestamp))
        return res or ''


class TimeMapList:
    def __init__(self):
        self.h = collections.defaultdict(lambda: [[0, None]])

    def set(self, key: str, value: str, timestamp: int) -> None:
        t, v = self.h[key][-1]
        if timestamp > t:
            self.h[key].append((timestamp, value))
        else:
            self.h[key][-1] = (timestamp, value)
            self.h[key].append((t, v))

    def get(self, key: str, timestamp: int) -> str:
        bucket = self.h.get(key)

        if not bucket:
            return ''

        i = len(bucket)-1
        while i >= 0:
            if bucket[i][0] <= timestamp:
                return bucket[i][1] or ''
            i -= 1

        return ''

        # Your TimeMap object will be instantiated and called as such:
        # obj = TimeMap()
        # obj.set(key,value,timestamp)
        # param_2 = obj.get(key,timestamp)
["TimeMap", "set", "set", "get", "get", "get", "get", "get"]
[
    # set
    ["love", "high", 10],
    ["love", "low", 20],
    #  get
    ["love", 5],
    ["love", 10],
    ["love", 15],
    ["love", 20],
    ["love", 25]]


def test1():
    timeMap = TimeMapTuple()
    res = [None, None, None]

    timeMap.set("love", "high", 10)
    timeMap.set("love", "low", 20)

    res.append(timeMap.get("love", 5))
    res.append(timeMap.get("love", 10))
    res.append(timeMap.get("love", 15))
    res.append(timeMap.get("love", 20))
    res.append(timeMap.get("love", 25))

    print(res)


def test2():
    timeMap = TimeMapList()
    res = [None, None, None]

    timeMap.set("love", "high", 10)
    timeMap.set("love", "low", 20)

    res.append(timeMap.get("love", 5))
    res.append(timeMap.get("love", 10))
    res.append(timeMap.get("love", 15))
    res.append(timeMap.get("love", 20))
    res.append(timeMap.get("love", 25))

    print(res)


args_parser = argparse.ArgumentParser()
args_parser.add_argument('--test',  action='store_true',
                         default=False, required=False)

args = args_parser.parse_args()

if args.test:
    test1()
    test2()

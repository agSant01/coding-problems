import argparse
import collections
from typing import Dict, List, Tuple


class UndergroundSystem:
    def __init__(self):
        # (start, end): [totalTime, samples]
        self.station_times: Dict[Tuple[str, str], List[int, int]] = collections.defaultdict(
            lambda: [0, 0])
        # id: (stationName, checkInTime)
        self.current_passengers: Dict[int, Tuple[str, int]] = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.current_passengers:
            return
        self.current_passengers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.current_passengers:
            return
        startStation, checkInTime = self.current_passengers[id]

        self.current_passengers.pop(id)

        self.station_times[(startStation, stationName)][0] += t-checkInTime
        self.station_times[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, samples = self.station_times[(startStation, endStation)]
        if samples == 0:
            return 0
        return totalTime/samples


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

def test1():
    undergroundSystem = UndergroundSystem()

    # Customer 10 "Leyton" -> "Paradise" in 8-3 = 5
    undergroundSystem.checkIn(10, "Leyton", 3)
    undergroundSystem.checkOut(10, "Paradise", 8)

    # return 5.00000, (5) / 1 = 5
    r1 = undergroundSystem.getAverageTime("Leyton", "Paradise")
    assert r1 == 5

    # Customer 5 "Leyton" -> "Paradise" in 16-10 = 6
    undergroundSystem.checkIn(5, "Leyton", 10)
    undergroundSystem.checkOut(5, "Paradise", 16)

    # return 5.50000, (5 + 6) / 2 = 5.5
    r2 = undergroundSystem.getAverageTime("Leyton", "Paradise")
    assert r2 == 5.5

    # Customer 2 "Leyton" -> "Paradise" in 30-21 = 9
    undergroundSystem.checkIn(2, "Leyton", 21)
    undergroundSystem.checkOut(2, "Paradise", 30)

    # return 6.66667, (5 + 6 + 9) / 3 = 6.66667
    r3 = undergroundSystem.getAverageTime("Leyton", "Paradise")
    assert r3 == (5 + 6 + 9) / 3

    print(r1, r2, r3)


args_parser = argparse.ArgumentParser()
args_parser.add_argument('--test',  action='store_true',
                         default=False, required=False)

args = args_parser.parse_args()

if args.test:
    test1()

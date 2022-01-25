import sys
from typing import List


class BestDays:
    def __init__(self, buy=None, sell=None) -> None:
        self.buy = buy
        self.sell = sell

    def __repr__(self) -> str:
        return f'BestDays {{ buy:{self.buy}, sell:{self.sell} }}'


def best_days(stock_prices: List[int]) -> List[BestDays]:

    buysAndSells = []

    bobj = BestDays()
    day = 1
    while day < len(stock_prices)-1:
        while day < len(stock_prices)-1 and stock_prices[day] >= stock_prices[day+1]:
            day += 1
        if bobj.buy is not None and stock_prices[day] < stock_prices[day-1]:
            bobj.sell = day-1
            buysAndSells.append(bobj)
            bobj = BestDays()
        elif bobj.buy is None and stock_prices[day] > stock_prices[day-1]:
            bobj.buy = day-1

        day += 1

    if bobj.buy is not None and bobj.buy < stock_prices[day]:
        bobj.sell = day
        buysAndSells.append(bobj)

    return buysAndSells


DAYS = [90, 170, 250, 300, 30, 525, 685, 90]
res = best_days(DAYS)
print(res)

DAYS = [90, 170, 250, 30, 300, 525, 90, 685, 90, 100]
res = best_days(DAYS)
print(res)

DAYS = [90, 170, 250, 30, 300, 525, 90, 685, 90, 100, 150]
res = best_days(DAYS)
print(res)

DAYS = [90, 170, 250, 30, 300, 525, 90, 685, 90, 100, 150, 80]
res = best_days(DAYS)
print(res)

DAYS = [90, 170, 250, 30, 300, 525, 100, 90, 685, 90, 100, 150, 80]
res = best_days(DAYS)
print(res)

DAYS = [90, 170, 250, 250, 30, 300, 525, 100, 90, 685, 90, 100, 150, 80]
res = best_days(DAYS)
print(res)


DAYS = [90, 170, 250, 300, 100, 525, 685, 90]
wins = 0
res = best_days(DAYS)
for t in res:
    print(DAYS[t.sell] - DAYS[t.buy])
    wins += DAYS[t.sell] - DAYS[t.buy]
print(res, wins)
print(DAYS[6]-DAYS[0])

DAYS = [90, 170, 250, 300, 80, 525, 685, 90]
wins = 0
res = best_days(DAYS)
for t in res:
    wins += DAYS[t.sell] - DAYS[t.buy]
print(res, wins)

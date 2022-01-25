"""
Given the daily values of a stock, write a program that will find how you can gain the most with a single buy-sell trade.

- Your function should be called bestDays and take one array of integers as an input.
- Daily stock values will be represented in an array of integers (arr[]) representing the stock price at the beginning or “opening bell” of each day.
- You may use the following as a test array, from day 0 through day 7: {17, 11, 60, 25, 150, 75, 31, 120}. In this case, purchasing on day one and selling on day four would yield the most profit.
- bestDays analyses historical data and returns when one should have bought and sold to maximize profit, it is not designed to predict the future. If you do manage to write a program that accurately predicts future stock market trends, congratulations, you’ll be very very rich.
- You are required to buy and sell only once.
- For the sake of this exercise, you will only ever be purchasing, owning, or selling one share.
- bestDays should return the day on which one should buy a share, followed by the day on which one should sell a share, as integers.
"""

import sys
from typing import List


class BestDays:
    def __init__(self, buy=None, sell=None) -> None:
        self.buy = buy
        self.sell = sell

    def __repr__(self) -> str:
        return f'BestDays {{ buy:{self.buy}, sell:{self.sell} }}'


def best_days(stock_prices: List[int]) -> BestDays:
    buy_day = 0
    buy_value = sys.maxsize
    sell_day = None
    profit = 0

    while buy_day < len(stock_prices)-1 and stock_prices[buy_day] >= stock_prices[buy_day+1]:
        buy_day += 1

    if buy_day == len(stock_prices)-1:
        return BestDays()

    for d in range(buy_day, len(stock_prices)):
        if stock_prices[d] < buy_value:
            buy_value = stock_prices[d]
            buy_day = d

    for d in range(buy_day, len(stock_prices)):
        nprofit = stock_prices[d] - buy_value
        if nprofit > profit:
            sell_day = d
            profit = nprofit

    return BestDays(buy=buy_day, sell=sell_day)


COLLECTION_1 = [17, 11, 60, 25, 150, 75, 31, 120]
res = best_days(COLLECTION_1)
print(res)

COLLECTION_1 = [17, 150, 60, 25, 11, 75, 31, 120]
res = best_days(COLLECTION_1)
print(res)

COLLECTION_1 = [150, 17, 60, 25, 11, 75, 31, 120]
res = best_days(COLLECTION_1)
print(res)

COLLECTION_1 = [150, 120, 17, 60, 25, 11, 75, 31]
res = best_days(COLLECTION_1)
print(res)

COLLECTION_1 = [150, 120, 100, 50, 20, 10, 5, 1]
res = best_days(COLLECTION_1)
print(res)


COLLECTION_1 = [150, 1, 100, 1, 50, 20, 10, 5, 1,  120, ]
res = best_days(COLLECTION_1)
print(res)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5896.股票价格波动.py
@Time    :   2021/10/10 10:48:06
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from sortedcontainers import SortedDict
from sortedcontainers import SortedList


class StockPrice:
    def __init__(self):
        self.stocks = SortedDict()
        self.prices = SortedList()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.stocks:
            self.prices.remove(self.stocks[timestamp])

        self.stocks[timestamp] = price
        self.prices.add(price)

    def current(self) -> int:
        return self.stocks.peekitem()[1]

    def maximum(self) -> int:
        return self.prices[-1]

    def minimum(self) -> int:
        return self.prices[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

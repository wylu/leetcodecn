#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5731.座位预约管理系统.py
@Time    :   2021/05/01 22:37:13
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import heapq


class SeatManager:
    def __init__(self, n: int):
        self.pq = list(range(1, n + 1))
        heapq.heapify(self.pq)

    def reserve(self) -> int:
        return heapq.heappop(self.pq)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.pq, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

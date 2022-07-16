#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   041.滑动窗口的平均值.py
@Time    :   2022/07/16 11:30:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """Initialize your data structure here."""
        self.queue = deque()
        self.total = 0
        self.size = size

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val
        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()
        return self.total / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

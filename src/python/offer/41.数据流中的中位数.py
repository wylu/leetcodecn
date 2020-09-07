#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   41.数据流中的中位数.py
@Time    :   2020/09/07 22:40:16
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
把整个数据分成两部分，max(第一部分) <= min(第二部分)。
第一部分用最大堆存储，第二部分用最小堆存储。

所有元素首先经过最小堆，再从最小堆中取出最小元素放入最大堆，这样可保证
max(最大堆) <= min(最小堆)
"""
import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxh = []
        self.minh = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxh, -heapq.heappushpop(self.minh, num))
        if len(self.maxh) > len(self.minh):
            heapq.heappush(self.minh, -heapq.heappop(self.maxh))

    def findMedian(self) -> float:
        if len(self.minh) > len(self.maxh):
            return self.minh[0]
        return (self.minh[0] + (-self.maxh[0])) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

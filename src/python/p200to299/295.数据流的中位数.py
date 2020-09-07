#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   295.数据流的中位数.py
@Time    :   2020/09/08 00:06:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# https://leetcode-cn.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (47.96%)
# Likes:    242
# Dislikes: 0
# Total Accepted:    21.9K
# Total Submissions: 45.6K
# Testcase Example:
# '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n'
# + '[[],[1],[2],[],[3],[]]'
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
#
# 例如，
#
# [2,3,4] 的中位数是 3
#
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
#
# 设计一个支持以下两种操作的数据结构：
#
#
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
#
#
# 示例：
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
#
# 进阶:
#
#
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
#
#
#
import heapq
"""
把整个数据分成两部分，max(第一部分) <= min(第二部分)。
第一部分用最大堆存储，第二部分用最小堆存储。

所有元素首先经过最小堆，再从最小堆中取出最小元素放入最大堆，这样可保证
max(最大堆) <= min(最小堆)
"""


# @lc code=start
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
# @lc code=end

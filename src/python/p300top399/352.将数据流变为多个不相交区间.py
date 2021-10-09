#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   352.将数据流变为多个不相交区间.py
@Time    :   2021/10/09 21:31:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=352 lang=python3
#
# [352] 将数据流变为多个不相交区间
#
# https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals/description/
#
# algorithms
# Hard (66.97%)
# Likes:    135
# Dislikes: 0
# Total Accepted:    17K
# Total Submissions: 25.4K
# Testcase Example:
# '["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]\n'
# + '[[],[1],[],[3],[],[7],[],[2],[],[6],[]]'
#
#  给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。
#
# 实现 SummaryRanges 类：
#
#
#
#
# SummaryRanges() 使用一个空数据流初始化对象。
# void addNum(int val) 向数据流中加入整数 val 。
# int[][] getIntervals() 以不相交区间 [starti, endi] 的列表形式返回对数据流中整数的总结。
#
#
#
#
# 示例：
#
#
# 输入：
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals",
# "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# 输出：
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7,
# 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
#
# 解释：
# SummaryRanges summaryRanges = new SummaryRanges();
# summaryRanges.addNum(1);      // arr = [1]
# summaryRanges.getIntervals(); // 返回 [[1, 1]]
# summaryRanges.addNum(3);      // arr = [1, 3]
# summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      // arr = [1, 3, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]
#
#
#
#
# 提示：
#
#
# 0 <= val <= 10^4
# 最多调用 addNum 和 getIntervals 方法 3 * 10^4 次
#
#
#
#
#
#
# 进阶：如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?
#
#
import bisect
from typing import List


# @lc code=start
class SummaryRanges:
    def __init__(self):
        self.nums = []

    def addNum(self, val: int) -> None:
        idx = bisect.bisect_left(self.nums, val)
        if idx == len(self.nums) or self.nums[idx] != val:
            self.nums.insert(idx, val)

    def getIntervals(self) -> List[List[int]]:
        if not self.nums:
            return []

        res = []
        begin = end = self.nums[0]
        for i in range(1, len(self.nums)):
            if self.nums[i] == end + 1:
                end = self.nums[i]
            else:
                res.append([begin, end])
                begin = end = self.nums[i]

        res.append([begin, end])

        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
# @lc code=end

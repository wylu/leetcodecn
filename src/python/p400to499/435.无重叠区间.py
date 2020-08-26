#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   435.无重叠区间.py
@Time    :   2020/08/26 13:08:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#
# https://leetcode-cn.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (45.93%)
# Likes:    191
# Dislikes: 0
# Total Accepted:    23.1K
# Total Submissions: 50.2K
# Testcase Example:  '[[1,2]]'
#
# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
#
# 注意:
#
#
# 可以认为区间的终点总是大于它的起点。
# 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
#
#
# 示例 1:
#
#
# 输入: [ [1,2], [2,3], [3,4], [1,3] ]
#
# 输出: 1
#
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
#
#
# 示例 2:
#
#
# 输入: [ [1,2], [1,2], [1,2] ]
#
# 输出: 2
#
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
#
#
# 示例 3:
#
#
# 输入: [ [1,2], [2,3] ]
#
# 输出: 0
#
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
#
#
#
from typing import List
"""
方法一：Dynamic Programming

State:
  dp[i]: 表示前 i+1 区间的最长无重叠的长度

方法二：贪心
"""


# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        n = len(intervals)
        ans, cur = 0, -0x8FFFFFFF
        for s, e in intervals:
            if s >= cur:
                ans += 1
                cur = e

        return n - ans


# @lc code=end

# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         if not intervals:
#             return 0

#         intervals.sort(key=lambda x: x[1])

#         n = len(intervals)
#         dp = [1] * n
#         ans = 1
#         for i in range(1, n):
#             for j in range(i - 1, -1, -1):
#                 if intervals[j][1] <= intervals[i][0]:
#                     # 不移除 intervals[i]
#                     dp[i] = dp[j] + 1
#                     break
#             # 选择移除或不移除 intervals[i]
#             dp[i] = max(dp[i], dp[i - 1])
#             ans = max(ans, dp[i])

#         return n - ans

if __name__ == '__main__':
    solu = Solution()
    print(solu.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(solu.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))

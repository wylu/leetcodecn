#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1109.航班预订统计.py
@Time    :   2020/09/21 23:23:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#
# https://leetcode-cn.com/problems/corporate-flight-bookings/description/
#
# algorithms
# Medium (47.58%)
# Likes:    88
# Dislikes: 0
# Total Accepted:    14.5K
# Total Submissions: 30.4K
# Testcase Example:  '[[1,2,10],[2,3,20],[2,5,25]]\n5'
#
# 这里有 n 个航班，它们分别从 1 到 n 进行编号。
#
# 我们这儿有一份航班预订表，表中第 i 条预订记录 bookings[i] = [i, j, k] 意味着我们在从 i 到 j 的每个航班上预订了 k
# 个座位。
#
# 请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数。
#
#
#
# 示例：
#
# 输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
# 输出：[10,55,45,25,25]
#
#
#
#
# 提示：
#
#
# 1 <= bookings.length <= 20000
# 1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
# 1 <= bookings[i][2] <= 10000
#
#
#
from typing import List
"""
差分序列
"""


# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]],
                           n: int) -> List[int]:
        d = [0] * n

        for i, j, k in bookings:
            d[i - 1] += k
            if j - 1 < n - 1:
                d[j] -= k

        for i in range(1, n):
            d[i] += d[i - 1]

        return d


# @lc code=end

# class Solution:
#     def corpFlightBookings(self, bookings: List[List[int]],
#                            n: int) -> List[int]:
#         a = [0] * (n + 1)
#         d = [0] * (n + 1)

#         for i, j, k in bookings:
#             d[i] += k
#             if j < n:
#                 d[j + 1] -= k

#         for i in range(1, n + 1):
#             a[i] = d[i] + a[i - 1]

#         return a[1:]

if __name__ == '__main__':
    solu = Solution()
    print(solu.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))

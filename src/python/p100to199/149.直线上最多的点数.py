#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   149.直线上最多的点数.py
@Time    :   2021/06/24 09:10:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
# https://leetcode-cn.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (26.96%)
# Likes:    260
# Dislikes: 0
# Total Accepted:    25.9K
# Total Submissions: 96.7K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
#
#
#
# 示例 1：
#
#
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：3
#
#
# 示例 2：
#
#
# 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出：4
#
#
#
#
# 提示：
#
#
# 1 <= points.length <= 300
# points[i].length == 2
# -10^4 <= xi, yi <= 10^4
# points 中的所有点 互不相同
#
#
#
from collections import defaultdict
from typing import List
"""
已知直线上两点求直线的一般式方程

已知直线上的两点 P1(x1,y1) P2(x2,y2)，P1 P2 两点不重合。
则直线的一般式方程 Ax + By + C = 0 中，A B C 分别等于：

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

方法一：朴素解法（枚举直线 + 枚举统计）
我们知道，两个点可以确定一条线。

因此一个朴素的做法是先枚举两条点（确定一条线），然后检查其余点是否落在该线中。

为了避免除法精度问题，当我们枚举两个点 i 和 j 时，不直接计算其对应直线的
斜率和截距，而是通过判断 i 和 j 与第三个点 k 形成的两条直线斜率是否相等
（斜率相等的两条直线要么平行，要么重合，平行需要 4 个点来唯一确定，我们只有
3 个点，所以可以直接判定两直线重合）。

    (x1, y1), (x2, y2), (x3, y3)

    k1 = (y2 - y1) / (x2 - x1)
    k2 = (y3 - y1) / (x3 - x1)

    k1 = k2  ->  (y2 - y1) / (x2 - x1) = (y3 - y1) / (x3 - x1)
             ->  (y2 - y1) * (x3 - x1) = (y3 - y1) * (x2 - x1)

方法二：优化（枚举直线 + 哈希表统计）
根据「朴素解法」的思路，枚举所有直线的过程不可避免，但统计点数的过程可以优化。

具体的，我们可以先枚举所有可能出现的 直线斜率（根据两点确定一条直线，即枚举
所有的「点对」），使用「哈希表」统计所有 斜率 对应的点的数量，在所有值中取个
max 即是答案。

一些细节：在使用「哈希表」进行保存时，为了避免精度问题，我们直接使用字符串
进行保存，同时需要将 斜率 约干净。
"""


# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans, n = 1, len(points)

        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        for i in range(n):
            lines = defaultdict(int)
            cnt = 0  # 由当前点 i 发出的直线所经过的最多点数量
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                a, b = x1 - x2, y1 - y2
                d = gcd(a, b)
                k = (a // d, b // d)
                lines[k] += 1
                cnt = max(cnt, lines[k])

            ans = max(ans, cnt + 1)

        return ans


# @lc code=end

# 方法一
# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
#         ans, n = 1, len(points)

#         for i in range(n):
#             x1, y1 = points[i]
#             for j in range(i + 1, n):
#                 cnt = 2
#                 x2, y2 = points[j]
#                 for k in range(j + 1, n):
#                     x3, y3 = points[k]
#                     if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
#                         cnt += 1
#                 ans = max(ans, cnt)

#         return ans

# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
#         lines, n = {}, len(points)
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 x1, y1 = points[i]
#                 x2, y2 = points[j]
#                 A = y2 - y1
#                 B = x1 - x2
#                 C = x2 * y1 - x1 * y2
#                 line = (A, B, C)
#                 if line not in lines:
#                     lines[line] = 0

#         ans = 1
#         for x, y in points:
#             for line in lines.keys():
#                 A, B, C = line
#                 if A * x + B * y + C == 0:
#                     lines[line] += 1
#                 ans = max(ans, lines[line])

#         return ans

if __name__ == '__main__':
    solu = Solution()
    points = [[1, 1], [2, 2], [3, 3]]
    print(solu.maxPoints(points))

    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    print(solu.maxPoints(points))

    points = [[0, 0]]
    print(solu.maxPoints(points))

    points = [[0, 0], [2, 2], [-1, -1]]
    print(solu.maxPoints(points))

    points = [[2, 3], [3, 3], [-5, 3]]
    print(solu.maxPoints(points))

    points = [[3, 2], [3, 3], [3, -5]]
    print(solu.maxPoints(points))

    points = [[9, -25], [-4, 1], [-1, 5], [-7, 7]]
    print(solu.maxPoints(points))

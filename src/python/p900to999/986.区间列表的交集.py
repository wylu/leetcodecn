#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   986.区间列表的交集.py
@Time    :   2020/10/16 10:28:14
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#
# https://leetcode-cn.com/problems/interval-list-intersections/description/
#
# algorithms
# Medium (65.37%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    10.2K
# Total Submissions: 15.5K
# Testcase Example:
# '[[0,2],[5,10],[13,23],[24,25]]\n[[1,5],[8,12],[15,24],[25,26]]'
#
# 给定两个由一些 闭区间 组成的列表，每个区间列表都是成对不相交的，并且已经排序。
#
# 返回这两个区间列表的交集。
#
# （形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <=
# b。两个闭区间的交集是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。）
#
#
#
# 示例：
#
#
#
# 输入：A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# 输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#
#
#
#
# 提示：
#
#
# 0 <= A.length < 1000
# 0 <= B.length < 1000
# 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
#
#
#
from typing import List
"""
方法：归并区间

思路

我们称 b 为区间 [a, b] 的末端点。在两个数组给定的所有区间中，假设拥有
最小末端点的区间是 A[0]。（为了不失一般性，该区间出现在数组 A 中)

然后，在数组 B 的区间中， A[0] 只可能与数组 B 中的至多一个区间相交。
（如果 B 中存在两个区间均与 A[0] 相交，那么它们将共同包含 A[0] 的末端点，
但是 B 中的区间应该是不相交的，所以存在矛盾）

算法

如果 A[0] 拥有最小的末端点，那么它只可能与 B[0] 相交。然后我们就可以删除
区间 A[0]，因为它不能与其他任何区间再相交了。相似的，如果 B[0] 拥有最小
的末端点，那么它只可能与区间 A[0] 相交，然后我们就可以将 B[0] 删除，因为
它无法再与其他区间相交了。我们用两个指针 i 与 j 来模拟完成删除 A[0] 或
B[0] 的操作。
"""


# @lc code=start
class Solution:
    def intervalIntersection(self, a: List[List[int]],
                             b: List[List[int]]) -> List[List[int]]:
        ans = []
        i, j, na, nb = 0, 0, len(a), len(b)

        while i < na and j < nb:
            lo = max(a[i][0], b[j][0])
            hi = min(a[i][1], b[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            if a[i][1] < b[j][1]:
                i += 1
            else:
                j += 1

        return ans


# @lc code=end

# class Solution:
#     def intervalIntersection(self, a: List[List[int]],
#                              b: List[List[int]]) -> List[List[int]]:
#         if not a or not b:
#             return []

#         c = a + b
#         c.sort()

#         ans = []
#         pe = c[0][1]
#         for i in range(1, len(c)):
#             cs, ce = c[i]
#             if cs > pe:
#                 pe = ce
#             else:
#                 ans.append([cs, min(ce, pe)])
#                 if ce > pe:
#                     pe = ce

#         return ans

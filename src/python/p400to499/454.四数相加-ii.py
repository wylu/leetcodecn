#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   454.四数相加-ii.py
@Time    :   2020/09/21 19:50:33
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#
# https://leetcode-cn.com/problems/4sum-ii/description/
#
# algorithms
# Medium (56.22%)
# Likes:    199
# Dislikes: 0
# Total Accepted:    27.8K
# Total Submissions: 49.5K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] +
# D[l] = 0。
#
# 为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -2^28 到 2^28 - 1
# 之间，最终结果不会超过 2^31 - 1 。
#
# 例如:
#
#
# 输入:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# 输出:
# 2
#
# 解释:
# 两个元组如下:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
#
#
#
from typing import List
"""
哈希表优化
"""


# @lc code=start
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int],
                     D: List[int]) -> int:
        ab = {}
        for x in A:
            for y in B:
                z = x + y
                ab[z] = ab.get(z, 0) + 1

        ans = 0
        for x in C:
            for y in D:
                z = 0 - (x + y)
                ans += ab.get(z, 0)

        return ans


# @lc code=end

# class Solution:
#     def fourSumCount(self, A: List[int], B: List[int], C: List[int],
#                      D: List[int]) -> int:
#         def merge(x: List[int], y: List[int]) -> dict:
#             z = {}
#             for i in x:
#                 for j in y:
#                     k = i + j
#                     z[k] = z.get(k, 0) + 1
#             return z

#         ab = merge(A, B)
#         cd = merge(C, D)

#         ans = 0
#         for num, cnt in cd.items():
#             ans += cnt * ab.get(0 - num, 0)

#         return ans

if __name__ == '__main__':
    solu = Solution()
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(solu.fourSumCount(A, B, C, D))

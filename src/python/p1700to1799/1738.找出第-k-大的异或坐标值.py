#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1738.找出第-k-大的异或坐标值.py
@Time    :   2021/05/19 22:16:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1738 lang=python3
#
# [1738] 找出第 K 大的异或坐标值
#
# https://leetcode-cn.com/problems/find-kth-largest-xor-coordinate-value/description/
#
# algorithms
# Medium (65.34%)
# Likes:    67
# Dislikes: 0
# Total Accepted:    23K
# Total Submissions: 35.2K
# Testcase Example:  '[[5,2],[1,6]]\n1'
#
# 给你一个二维矩阵 matrix 和一个整数 k ，矩阵大小为 m x n 由非负整数组成。
#
# 矩阵中坐标 (a, b) 的 值 可由对所有满足 0 <= i <= a < m 且 0 <= j <= b < n 的元素
# matrix[i][j]（下标从 0 开始计数）执行异或运算得到。
#
# 请你找出 matrix 的所有坐标中第 k 大的值（k 的值从 1 开始计数）。
#
#
#
# 示例 1：
#
# 输入：matrix = [[5,2],[1,6]], k = 1
# 输出：7
# 解释：坐标 (0,1) 的值是 5 XOR 2 = 7 ，为最大的值。
#
# 示例 2：
#
# 输入：matrix = [[5,2],[1,6]], k = 2
# 输出：5
# 解释：坐标 (0,0) 的值是 5 = 5 ，为第 2 大的值。
#
# 示例 3：
#
# 输入：matrix = [[5,2],[1,6]], k = 3
# 输出：4
# 解释：坐标 (1,0) 的值是 5 XOR 1 = 4 ，为第 3 大的值。
#
# 示例 4：
#
# 输入：matrix = [[5,2],[1,6]], k = 4
# 输出：0
# 解释：坐标 (1,1) 的值是 5 XOR 2 XOR 1 XOR 6 = 0 ，为第 4 大的值。
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 0 <= matrix[i][j] <= 10^6
# 1 <= k <= m * n
#
#
#
# import heapq
from typing import List


# @lc code=start
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        m, n = len(matrix), len(matrix[0])
        xors = [0] * n
        for i in range(m):
            cur = 0
            for j in range(n):
                cur ^= matrix[i][j]
                xors[j] ^= cur
                pq.append(xors[j])
        pq.sort()
        return pq[-k]


# @lc code=end

# class Solution:
#     def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
#         pq = []
#         m, n = len(matrix), len(matrix[0])
#         xors = [0] * n
#         for i in range(m):
#             cur = 0
#             for j in range(n):
#                 cur ^= matrix[i][j]
#                 xors[j] ^= cur
#                 heapq.heappush(pq, xors[j])
#                 if len(pq) > k:
#                     heapq.heappop(pq)
#         return heapq.heappop(pq)

if __name__ == '__main__':
    solu = Solution()
    print(solu.kthLargestValue(matrix=[[5, 2], [1, 6]], k=1))
    print(solu.kthLargestValue(matrix=[[5, 2], [1, 6]], k=2))
    print(solu.kthLargestValue(matrix=[[5, 2], [1, 6]], k=3))
    print(solu.kthLargestValue(matrix=[[5, 2], [1, 6]], k=4))

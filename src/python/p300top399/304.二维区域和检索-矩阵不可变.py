#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   304.二维区域和检索-矩阵不可变.py
@Time    :   2021/03/02 11:58:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#
# https://leetcode-cn.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (51.59%)
# Likes:    185
# Dislikes: 0
# Total Accepted:    28.6K
# Total Submissions: 55.6K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +
# '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
#
#
# 上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。
#
#
#
# 示例：
#
#
# 给定 matrix = [
# ⁠ [3, 0, 1, 4, 2],
# ⁠ [5, 6, 3, 2, 1],
# ⁠ [1, 2, 0, 1, 5],
# ⁠ [4, 1, 0, 1, 7],
# ⁠ [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
#
#
#
#
# 提示：
#
#
# 你可以假设矩阵不可变。
# 会多次调用 sumRegion 方法。
# 你可以假设 row1 ≤ row2 且 col1 ≤ col2 。
#
#
#
from typing import List


# @lc code=start
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])
        self.ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.ps[i + 1][j + 1] = (self.ps[i][j + 1] +
                                         self.ps[i + 1][j] - self.ps[i][j])
                self.ps[i + 1][j + 1] += matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.ps[row2 + 1][col2 + 1] - self.ps[row1][col2 + 1] -
                self.ps[row2 + 1][col1] + self.ps[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   867.转置矩阵.py
@Time    :   2021/02/25 14:14:13
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#
# https://leetcode-cn.com/problems/transpose-matrix/description/
#
# algorithms
# Easy (68.33%)
# Likes:    169
# Dislikes: 0
# Total Accepted:    59.9K
# Total Submissions: 87.7K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
#
# 矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
#
#
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[1,4,7],[2,5,8],[3,6,9]]
#
#
# 示例 2：
#
#
# 输入：matrix = [[1,2,3],[4,5,6]]
# 输出：[[1,4],[2,5],[3,6]]
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 10^5
# -10^9 <= matrix[i][j] <= 10^9
#
#
#
from typing import List


# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        return [[matrix[r][c] for r in range(m)] for c in range(n)]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(solu.transpose([[1, 2, 3], [4, 5, 6]]))

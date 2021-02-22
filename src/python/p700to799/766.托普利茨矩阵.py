#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   766.托普利茨矩阵.py
@Time    :   2021/02/22 22:18:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=766 lang=python3
#
# [766] 托普利茨矩阵
#
# https://leetcode-cn.com/problems/toeplitz-matrix/description/
#
# algorithms
# Easy (70.74%)
# Likes:    208
# Dislikes: 0
# Total Accepted:    45.2K
# Total Submissions: 64K
# Testcase Example:  '[[1,2,3,4],[5,1,2,3],[9,5,1,2]]'
#
# 给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。
#
# 如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# 输出：true
# 解释：
# 在上述矩阵中, 其对角线为:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
# 各条对角线上的所有元素均相同, 因此答案是 True 。
#
#
# 示例 2：
#
#
# 输入：matrix = [[1,2],[2,2]]
# 输出：false
# 解释：
# 对角线 "[1, 2]" 上的元素不同。
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 20
# 0 <= matrix[i][j] <= 99
#
#
#
#
# 进阶：
#
#
# 如果矩阵存储在磁盘上，并且内存有限，以至于一次最多只能将矩阵的一行加载到内存中，该怎么办？
# 如果矩阵太大，以至于一次只能将不完整的一行加载到内存中，该怎么办？
#
#
#
from typing import List


# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0 and matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    print(solu.isToeplitzMatrix(matrix))

    matrix = [[1, 2], [2, 2]]
    print(solu.isToeplitzMatrix(matrix))

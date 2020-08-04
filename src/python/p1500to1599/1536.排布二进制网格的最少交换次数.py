#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1536.排布二进制网格的最少交换次数.py
@Time    :   2020/08/04 17:36:37
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1536 lang=python3
#
# [1536] 排布二进制网格的最少交换次数
#
# https://leetcode-cn.com/problems/minimum-swaps-to-arrange-a-binary-grid/description/
#
# algorithms
# Medium (38.56%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 6.4K
# Testcase Example:  '[[0,0,1],[1,1,0],[1,0,0]]'
#
# 给你一个 n x n 的二进制网格 grid，每一次操作中，你可以选择网格的 相邻两行 进行交换。
#
# 一个符合要求的网格需要满足主对角线以上的格子全部都是 0 。
#
# 请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 -1 。
#
# 主对角线指的是从 (1, 1) 到 (n, n) 的这些格子。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[0,0,1],[1,1,0],[1,0,0]]
# 输出：3
#
#
# 示例 2：
#
#
#
# 输入：grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# 输出：-1
# 解释：所有行都是一样的，交换相邻行无法使网格符合要求。
#
#
# 示例 3：
#
#
#
# 输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
# 输出：0
#
#
#
#
# 提示：
#
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 200
# grid[i][j] 要么是 0 要么是 1 。
#
#
#
from typing import List


# @lc code=start
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        a = [0] * n
        for i in range(n):
            for j in range(n - 1, 0, -1):
                if grid[i][j] == 1:
                    a[i] = j
                    break

        ans = 0
        for i in range(n):
            j = i
            while j < n:
                if a[j] <= i:
                    break
                j += 1

            if j == n:
                return -1

            while j > i:
                a[j], a[j - 1] = a[j - 1], a[j]
                j -= 1
                ans += 1

        return ans


# @lc code=end

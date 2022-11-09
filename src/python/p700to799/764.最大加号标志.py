#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   764.最大加号标志.py
@Time    :   2022/11/09 14:10:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=764 lang=python3
#
# [764] 最大加号标志
#
# https://leetcode.cn/problems/largest-plus-sign/description/
#
# algorithms
# Medium (49.77%)
# Likes:    156
# Dislikes: 0
# Total Accepted:    15.3K
# Total Submissions: 28.8K
# Testcase Example:  '5\n[[4,2]]'
#
# 在一个 n x n 的矩阵 grid 中，除了在数组 mines 中给出的元素为 0，其他每个元素都为 1。mines[i] = [xi, yi]表示
# grid[xi][yi] == 0
#
# 返回  grid 中包含 1 的最大的 轴对齐 加号标志的阶数 。如果未找到加号标志，则返回 0 。
#
# 一个 k 阶由 1 组成的 “轴对称”加号标志 具有中心网格 grid[r][c] == 1 ，以及4个从中心向上、向下、向左、向右延伸，长度为
# k-1，由 1 组成的臂。注意，只有加号标志的所有网格要求为 1 ，别的网格可能为 0 也可能为 1 。
#
#
#
# 示例 1：
#
#
#
#
# 输入: n = 5, mines = [[4, 2]]
# 输出: 2
# 解释: 在上面的网格中，最大加号标志的阶只能是2。一个标志已在图中标出。
#
#
# 示例 2：
#
#
#
#
# 输入: n = 1, mines = [[0, 0]]
# 输出: 0
# 解释: 没有加号标志，返回 0 。
#
#
#
#
# 提示：
#
#
# 1 <= n <= 500
# 1 <= mines.length <= 5000
# 0 <= xi, yi < n
# 每一对 (xi, yi) 都 不重复​​​​​​​
#
#
#
from typing import List


# @lc code=start
class Solution:

    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines = set(tuple(item) for item in mines)

        left = [[-1] * n for _ in range(n)]
        right = [[n] * n for _ in range(n)]
        up = [[-1] * n for _ in range(n)]
        down = [[n] * n for _ in range(n)]

        for i in range(n):
            for j in range(1, n):
                if (i, j - 1) in mines:
                    left[i][j] = j - 1
                else:
                    left[i][j] = left[i][j - 1]
                if (i, n - j) in mines:
                    right[i][n - j - 1] = n - j
                else:
                    right[i][n - j - 1] = right[i][n - j]

        for i in range(1, n):
            for j in range(n):
                if (i - 1, j) in mines:
                    up[i][j] = i - 1
                else:
                    up[i][j] = up[i - 1][j]
                if (n - i, j) in mines:
                    down[n - i - 1][j] = n - i
                else:
                    down[n - i - 1][j] = down[n - i][j]

        ans = int(len(mines) < n * n)
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                if (i, j) not in mines:
                    k = min(j - left[i][j], right[i][j] - j, i - up[i][j],
                            down[i][j] - i)
                    ans = max(ans, k)

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.orderOfLargestPlusSign(5, [[4, 2]]))

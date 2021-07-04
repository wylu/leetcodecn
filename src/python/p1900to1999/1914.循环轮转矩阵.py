#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1914.循环轮转矩阵.py
@Time    :   2021/07/04 16:39:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1914 lang=python3
#
# [1914] 循环轮转矩阵
#
# https://leetcode-cn.com/problems/cyclically-rotating-a-grid/description/
#
# algorithms
# Medium (42.75%)
# Likes:    8
# Dislikes: 0
# Total Accepted:    2.8K
# Total Submissions: 6.6K
# Testcase Example:  '[[40,10],[30,20]]\n1'
#
# 给你一个大小为 m x n 的整数矩阵 grid​​​ ，其中 m 和 n 都是 偶数 ；另给你一个整数 k 。
#
# 矩阵由若干层组成，如下图所示，每种颜色代表一层：
#
#
#
# 矩阵的循环轮转是通过分别循环轮转矩阵中的每一层完成的。在对某一层进行一次循环旋转操作时，层中的每一个元素将会取代其 逆时针
# 方向的相邻元素。轮转示例如下：
#
# 返回执行 k 次循环轮转操作后的矩阵。
#
#
#
# 示例 1：
#
# 输入：grid = [[40,10],[30,20]], k = 1
# 输出：[[10,20],[40,30]]
# 解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。
#
# 示例 2：
# ⁠
#
# 输入：grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
# 输出：[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
# 解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 50
# m 和 n 都是 偶数
# 1 <= grid[i][j] <= 5000
# 1 <= k <= 10^9
#
#
#
from typing import List


# @lc code=start
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        def get_circle(c: int) -> List[int]:
            nums = []
            sx, ex, sy, ey = c, m - c - 1, c, n - c - 1
            for i in range(sy, ey + 1):
                nums.append(grid[sx][i])
            for i in range(sx + 1, ex + 1):
                nums.append(grid[i][ey])
            for i in range(ey - 1, sy - 1, -1):
                nums.append(grid[ex][i])
            for i in range(ex - 1, sx, -1):
                nums.append(grid[i][sy])
            return nums

        def put_circle(nums: List[int], k: int, c: int) -> None:
            nums = nums[k:] + nums[:k]
            nums.reverse()
            sx, ex, sy, ey = c, m - c - 1, c, n - c - 1
            for i in range(sy, ey + 1):
                grid[sx][i] = nums.pop()
            for i in range(sx + 1, ex + 1):
                grid[i][ey] = nums.pop()
            for i in range(ey - 1, sy - 1, -1):
                grid[ex][i] = nums.pop()
            for i in range(ex - 1, sx, -1):
                grid[i][sy] = nums.pop()

        for i in range(min(m, n) // 2):
            cnt = (m - i * 2) * 2 + (n - (i + 1) * 2) * 2
            put_circle(get_circle(i), k % cnt, i)

        return grid


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    grid = [[40, 10], [30, 20]]
    k = 1
    print(solu.rotateGrid(grid, k))

    grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    k = 2
    print(solu.rotateGrid(grid, k))

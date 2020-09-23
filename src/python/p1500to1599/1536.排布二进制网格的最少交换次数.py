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
"""
方法一：贪心算法

思路与算法

我们从上到下逐行确定，假设当前考虑到第 i 行，第 0,...,i−1 行都已经确定好。
按题意第 i 行满足的条件为末尾连续零的个数大于等于 n−i−1，那么我们考虑将
[i,...,n−1] 中的哪一行逐行交换到第 i 行。假设当前有多行都满足第 i 行的
条件，我们应该选择哪一行交换到第 i 行呢？为了令最后交换次数最少，我们
贪心地选择离第 i 行最近的那一行即可。

你可能会在想这样是否一定正确。我们可以考虑假设当前有若干行都能满足第 i 行，
那么这些行一定都满足第 i+1,...,n−1 的限制条件，也就是说能交换到第 i 行的
那些行一定也能交换到后面几行，因为随着行数的增加，限制条件越来越宽松。因此
不会存在贪心地选择后，后面出现无法放置的情况。

最后来看实现。为了避免每次判断当前行是否满足末尾连续零的个数的限制条件的
时候都要从后往前遍历当前行，造成不必要的时间消耗，我们需要先用 O(n^2) 的
操作预处理出每一行最后一个 1 所在的位置，记为 pos[i]。这样我们就可以按照
我们的策略模拟，从上到下逐行确定，对于第 i 行，只要找到第 i,...,n−1 行中
使得 pos[j] <= i 成立的最近的那一行 j，我们将这一行交换到第 i 行即可，
它对答案的贡献为 j−i。
"""


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

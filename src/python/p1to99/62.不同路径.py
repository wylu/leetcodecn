#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   62.不同路径.py
@Time    :   2020/10/13 11:23:16
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
# https://leetcode-cn.com/problems/unique-paths/description/
#
# algorithms
# Medium (62.41%)
# Likes:    715
# Dislikes: 0
# Total Accepted:    153.8K
# Total Submissions: 246.5K
# Testcase Example:  '3\n7'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 问总共有多少条不同的路径？
#
#
#
# 例如，上图是一个7 x 3 的网格。有多少可能的路径？
#
#
#
# 示例 1:
#
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
#
#
# 示例 2:
#
# 输入: m = 7, n = 3
# 输出: 28
#
#
#
# 提示：
#
#
# 1 <= m, n <= 100
# 题目数据保证答案小于等于 2 * 10 ^ 9
#
#
#
"""
Dynamic Programming

State:
  dp[i][j]: 到达 grid[i][j] 的可能的路径数

State Transition:
  dp[i][j] = dp[i-1][j] + dp[i][j-1]

Base Case:
  dp[i][0] = 1
  dp[0][j] = 1
"""


# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        for i in range(m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[n - 1]


# @lc code=end

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[0] * n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 if i == 0:
#                     dp[i][j] = 1
#                 elif j == 0:
#                     dp[i][j] = 1
#                 else:
#                     dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
#         return dp[m - 1][n - 1]

if __name__ == "__main__":
    solu = Solution()
    print(solu.uniquePaths(3, 2))
    print(solu.uniquePaths(7, 3))
    print(solu.uniquePaths(1, 1))

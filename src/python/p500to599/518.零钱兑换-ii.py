#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   518.零钱兑换-ii.py
@Time    :   2021/06/10 22:25:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
# https://leetcode-cn.com/problems/coin-change-2/description/
#
# algorithms
# Medium (63.02%)
# Likes:    514
# Dislikes: 0
# Total Accepted:    78.3K
# Total Submissions: 124.2K
# Testcase Example:  '5\n[1,2,5]'
#
# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
#
#
#
#
#
#
# 示例 1:
#
# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
#
# 示例 2:
#
# 输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
#
#
# 示例 3:
#
# 输入: amount = 10, coins = [10]
# 输出: 1
#
#
#
#
# 注意:
#
# 你可以假设：
#
#
# 0 <= amount (总金额) <= 5000
# 1 <= coin (硬币面额) <= 5000
# 硬币种类不超过 500 种
# 结果符合 32 位符号整数
#
#
#
from typing import List
"""
完全背包
https://oi-wiki.org/dp/knapsack/
"""


# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        f = [0] * (amount + 1)
        f[0] = 1

        for i in range(1, n + 1):
            for j in range(coins[i - 1], amount + 1):
                f[j] += f[j - coins[i - 1]]

        return f[amount]


# @lc code=end

# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)
#         f = [[0] * (amount + 1) for _ in range(n + 1)]
#         f[0][0] = 1

#         for i in range(1, n + 1):
#             for j in range(amount + 1):
#                 f[i][j] = f[i - 1][j]
#                 if j >= coins[i - 1]:
#                     f[i][j] += f[i][j - coins[i - 1]]

#         return f[n][amount]

if __name__ == '__main__':
    solu = Solution()
    print(solu.change(amount=5, coins=[1, 2, 5]))
    print(solu.change(amount=3, coins=[2]))
    print(solu.change(amount=10, coins=[10]))

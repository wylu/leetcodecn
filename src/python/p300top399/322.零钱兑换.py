#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   322.零钱兑换.py
@Time    :   2021/04/07 22:22:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (43.07%)
# Likes:    1189
# Dislikes: 0
# Total Accepted:    208.5K
# Total Submissions: 484.1K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
# 你可以认为每种硬币的数量是无限的。
#
#
#
# 示例 1：
#
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
#
# 示例 2：
#
#
# 输入：coins = [2], amount = 3
# 输出：-1
#
# 示例 3：
#
#
# 输入：coins = [1], amount = 0
# 输出：0
#
#
# 示例 4：
#
#
# 输入：coins = [1], amount = 1
# 输出：1
#
#
# 示例 5：
#
#
# 输入：coins = [1], amount = 2
# 输出：2
#
#
#
#
# 提示：
#
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
#
#
from typing import List
"""
Dynamic Programming
完全背包问题——填满容量为 amount 的背包最少需要多少硬币

State:
  dp[i]：表示填满容量为 i 的背包最少需要多少硬币

Initial State:
  因为硬币的数量一定不会超过 amount，而 amount <= 10^4，因此初始化
  数组值为 10001；
  dp[0] = 0

State Transition:
  dp[i] = min(dp[i], dp[i - coin] + 1)

当前填满容量 i 最少需要的硬币 = min(之前填满容量 i 最少需要的硬币,
                                 填满容量 i-coin 需要的硬币 + 1个当前硬币）

返回 dp[amount]，如果 dp[amount] 的值为 10001 没有变过，
说明找不到硬币组合，返回-1
"""


# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [10001] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == 10001 else dp[amount]


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.coinChange(coins=[1, 2, 5], amount=11))
    print(solu.coinChange(coins=[2], amount=3))
    print(solu.coinChange(coins=[1], amount=0))
    print(solu.coinChange(coins=[1], amount=1))
    print(solu.coinChange(coins=[1], amount=2))

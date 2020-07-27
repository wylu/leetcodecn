#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   309.最佳买卖股票时机含冷冻期.py
@Time    :   2020/07/27 23:15:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (56.80%)
# Likes:    479
# Dislikes: 0
# Total Accepted:    49.6K
# Total Submissions: 87.3K
# Testcase Example:  '[1,2,3,0,2]'
#
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
#
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
#
#
# 示例:
#
# 输入: [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
#
#

from typing import List
"""
Dynamic Programming

State:
  dp[i][0]: 表示第 i+1 天结束时，不持有股票，所能获得的最大利润。
  dp[i][1]: 表示第 i+1 天结束时，持有股票，所能获得的最大利润。

Initial State:
  dp[-1][0] = Integer.MIN_VALUE
  dp[0][0] = 0
  dp[0][1] = -prices[0]

State Transition:
  dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]), i > 0
  dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i]), i > 0
"""


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0

        # 优化空间复杂度
        # dpi20: dp[i-2][0], dpi10: dp[i-1][0], dpi11: dp[i-1][1]
        di20, di10, di11 = 0, 0, -prices[0]
        for i in range(1, len(prices)):
            tmp = di20
            di20 = di10
            di10 = max(di10, di11 + prices[i])
            di11 = max(di11, tmp - prices[i])

        return di10


# @lc code=end

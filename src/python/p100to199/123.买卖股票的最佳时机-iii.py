#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   123.买卖股票的最佳时机-iii.py
@Time    :   2020/07/26 23:36:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (43.97%)
# Likes:    455
# Dislikes: 0
# Total Accepted:    46.4K
# Total Submissions: 105.2K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
# 随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
#
# 示例 2:
#
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4
# 。
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#
#
# 示例 3:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
#
#

from typing import List
"""
Dynamic Programming

State:
  dp[i][k][0]: 表示第 i+1 天结束时，至今最多完成 k 笔交易，且不持有股票，
               所能获得的最大利润。
  dp[i][k][1]: 表示第 i+1 天结束时，至今最多完成 k 笔交易，且持有股票
               所能获得的最大利润。

Initial State:
  dp[0][0][0] = 0
  dp[0][0][1] = Integer.MIN_VALUE
  dp[0][k][0] = 0, (1<= k <=2)
  dp[0][k][1] = -prices[0], (1<= k <=2)

State Transition:
  dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i]), i > 0
  dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i]), i > 0
"""


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0, -prices[0]] for _ in range(3)]

        for i in range(1, n):
            for k in range(1, 3):
                k0 = max(dp[k][0], dp[k][1] + prices[i])
                k1 = max(dp[k][1], dp[k - 1][0] - prices[i])
                dp[k][0], dp[k][1] = k0, k1

        return dp[2][0]


# @lc code=end

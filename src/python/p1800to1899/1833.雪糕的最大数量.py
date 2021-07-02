#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1833.雪糕的最大数量.py
@Time    :   2021/07/02 13:45:16
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1833 lang=python3
#
# [1833] 雪糕的最大数量
#
# https://leetcode-cn.com/problems/maximum-ice-cream-bars/description/
#
# algorithms
# Medium (79.12%)
# Likes:    30
# Dislikes: 0
# Total Accepted:    17.9K
# Total Submissions: 22.6K
# Testcase Example:  '[1,3,2,4,1]\n7'
#
# 夏日炎炎，小男孩 Tony 想买一些雪糕消消暑。
#
# 商店中新到 n 支雪糕，用长度为 n 的数组 costs 表示雪糕的定价，其中 costs[i] 表示第 i 支雪糕的现金价格。Tony 一共有
# coins 现金可以用于消费，他想要买尽可能多的雪糕。
#
# 给你价格数组 costs 和现金量 coins ，请你计算并返回 Tony 用 coins 现金能够买到的雪糕的 最大数量 。
#
# 注意：Tony 可以按任意顺序购买雪糕。
#
#
#
# 示例 1：
#
# 输入：costs = [1,3,2,4,1], coins = 7
# 输出：4
# 解释：Tony 可以买下标为 0、1、2、4 的雪糕，总价为 1 + 3 + 2 + 1 = 7
#
#
# 示例 2：
#
# 输入：costs = [10,6,8,7,7,8], coins = 5
# 输出：0
# 解释：Tony 没有足够的钱买任何一支雪糕。
#
#
# 示例 3：
#
# 输入：costs = [1,6,3,1,2,5], coins = 20
# 输出：6
# 解释：Tony 可以买下所有的雪糕，总价为 1 + 6 + 3 + 1 + 2 + 5 = 18 。
#
#
#
#
# 提示：
#
#
# costs.length == n
# 1 <= n <= 10^5
# 1 <= costs[i] <= 10^5
# 1 <= coins <= 10^8
#
#
#
# from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans = 0
        costs.sort()
        for cost in costs:
            if coins < cost:
                break
            ans += 1
            coins -= cost
        return ans


# @lc code=end

# class Solution:
#     def maxIceCream(self, costs: List[int], coins: int) -> int:
#         counter = defaultdict(int)
#         max_cost = 0
#         for cost in costs:
#             counter[cost] += 1
#             max_cost = max(max_cost, cost)

#         ans = 0
#         for cost in range(1, max_cost+1):
#             if coins < cost:
#                 break
#             if counter[cost]:
#                 num = min(coins // cost, counter[cost])
#                 ans += num
#                 coins -= num * cost
#         return ans

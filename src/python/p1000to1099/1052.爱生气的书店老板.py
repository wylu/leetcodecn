#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1052.爱生气的书店老板.py
@Time    :   2021/02/23 09:03:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#
# https://leetcode-cn.com/problems/grumpy-bookstore-owner/description/
#
# algorithms
# Medium (55.00%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    12.2K
# Total Submissions: 22.2K
# Testcase Example:  '[1,0,1,2,1,1,7,5]\n[0,1,0,1,0,1,0,1]\n3'
#
# 今天，书店老板有一家店打算试营业 customers.length
# 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
#
# 在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。
# 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
#
# 书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
#
# 请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
#
#
# 示例：
#
# 输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# 输出：16
# 解释：
# 书店老板在最后 3 分钟保持冷静。
# 感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
#
#
#
#
# 提示：
#
#
# 1 <= X <= customers.length == grumpy.length <= 20000
# 0 <= customers[i] <= 1000
# 0 <= grumpy[i] <= 1
#
#
#
from typing import List


# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int],
                     X: int) -> int:
        tot = 0
        for cus, gru in zip(customers, grumpy):
            if gru == 0:
                tot += cus

        cur, n = 0, len(customers)
        for i in range(min(X, n)):
            cur += customers[i] * grumpy[i]

        increase = cur
        for i in range(X, n):
            cur += customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
            increase = max(increase, cur)

        return tot + increase


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    X = 3
    print(solu.maxSatisfied(customers, grumpy, X))

    customers = [4, 10, 10]
    grumpy = [1, 1, 0]
    X = 2
    print(solu.maxSatisfied(customers, grumpy, X))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   746.使用最小花费爬楼梯.py
@Time    :   2020/12/21 22:01:08
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#
# https://leetcode-cn.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (54.01%)
# Likes:    474
# Dislikes: 0
# Total Accepted:    74.7K
# Total Submissions: 138.3K
# Testcase Example:  '[0,0,0,0]'
#
# 数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
#
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
#
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
#
# 示例 1:
#
# 输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
#
#
# 示例 2:
#
# 输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
#
#
# 注意：
#
#
# cost 的长度将会在 [2, 1000]。
# 每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。
#
#
#
from typing import List
"""
f0, f1 = cost[0], cost[1]
f2 = min(f0, f1) + cost[i]
f0, f1 = f1, f2
"""


# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f0, f1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            f0, f1 = f1, min(f0, f1) + cost[i]
        return min(f0, f1)


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.minCostClimbingStairs([10, 15, 20]))
    print(solu.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

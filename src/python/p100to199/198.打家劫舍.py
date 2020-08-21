#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   198.打家劫舍.py
@Time    :   2020/08/02 16:28:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# https://leetcode-cn.com/problems/house-robber/description/
#
# algorithms
# Easy (46.02%)
# Likes:    970
# Dislikes: 0
# Total Accepted:    160.6K
# Total Submissions: 348.1K
# Testcase Example:  '[1,2,3,1]'
#
#
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
#
#
#
# 示例 1：
#
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
#
# 示例 2：
#
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
#
#
from typing import List
"""
Dynamic Programing

State:
  0 <= i < n-1
  dp[i][0]: 表示前 i+1 个房屋且不偷窃 i+1 号房屋所能得到的最高金额
  dp[i][1]: 表示前 i+1 个房屋且偷窃 i+1 号房屋所能得到的最高金额

Initial State:
  dp[0][0] = 0
  dp[0][1] = nums[0]

State Transition:
  0 <= i < n-1
  dp[i+1][0] = max(dp[i][0], dp[i][1])
  dp[i+1][1] = dp[i][0] + nums[i+1]

空间复杂度优化：
通过状态转移方程可知，当前状态的计算只与前一个状态有关，所以只需保留
前一个状态即可。
"""


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        f0, f1 = 0, nums[0]
        for i in range(len(nums) - 1):
            f0, f1 = max(f0, f1), f0 + nums[i + 1]

        return max(f0, f1)


# @lc code=end

# Version 1
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         n = len(nums)
#         dp = [[0, 0] for _ in range(n)]
#         dp[0][1] = nums[0]

#         for i in range(n - 1):
#             dp[i + 1][0] = max(dp[i][0], dp[i][1])
#             dp[i + 1][1] = dp[i][0] + nums[i + 1]

#         return max(dp[n - 1])

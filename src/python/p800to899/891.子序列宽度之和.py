#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   891.子序列宽度之和.py
@Time    :   2022/11/18 19:38:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=891 lang=python3
#
# [891] 子序列宽度之和
#
# https://leetcode.cn/problems/sum-of-subsequence-widths/description/
#
# algorithms
# Hard (44.18%)
# Likes:    144
# Dislikes: 0
# Total Accepted:    13.3K
# Total Submissions: 30.1K
# Testcase Example:  '[2,1,3]'
#
# 一个序列的 宽度 定义为该序列中最大元素和最小元素的差值。
#
# 给你一个整数数组 nums ，返回 nums 的所有非空 子序列 的 宽度之和 。由于答案可能非常大，请返回对 10^9 + 7 取余 后的结果。
#
# 子序列 定义为从一个数组里删除一些（或者不删除）元素，但不改变剩下元素的顺序得到的数组。例如，[3,6,2,7] 就是数组 [0,3,1,6,2,2,7]
# 的一个子序列。
#
#
#
# 示例 1：
#
#
# 输入：nums = [2,1,3]
# 输出：6
# 解释：子序列为 [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3] 。
# 相应的宽度是 0, 0, 0, 1, 1, 2, 2 。
# 宽度之和是 6 。
#
#
# 示例 2：
#
#
# 输入：nums = [2]
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
#
#
#
from typing import List


# @lc code=start
class Solution:

    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        pow2 = [0] * n
        pow2[0] = 1
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = 0
        for i, x in enumerate(nums):
            ans += (pow2[i] - pow2[n - i - 1]) * x

        return ans % MOD


# @lc code=end

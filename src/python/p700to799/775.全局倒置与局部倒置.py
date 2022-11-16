#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   775.全局倒置与局部倒置.py
@Time    :   2022/11/16 19:48:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=775 lang=python3
#
# [775] 全局倒置与局部倒置
#
# https://leetcode.cn/problems/global-and-local-inversions/description/
#
# algorithms
# Medium (48.28%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    24.7K
# Total Submissions: 51.1K
# Testcase Example:  '[1,0,2]'
#
# 给你一个长度为 n 的整数数组 nums ，表示由范围 [0, n - 1] 内所有整数组成的一个排列。
#
# 全局倒置 的数目等于满足下述条件不同下标对 (i, j) 的数目：
#
#
# 0 <= i < j < n
# nums[i] > nums[j]
#
#
# 局部倒置 的数目等于满足下述条件的下标 i 的数目：
#
#
# 0 <= i < n - 1
# nums[i] > nums[i + 1]
#
#
# 当数组 nums 中 全局倒置 的数量等于 局部倒置 的数量时，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,0,2]
# 输出：true
# 解释：有 1 个全局倒置，和 1 个局部倒置。
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,0]
# 输出：false
# 解释：有 2 个全局倒置，和 1 个局部倒置。
#
#
#
# 提示：
#
#
# n == nums.length
# 1 <= n <= 10^5
# 0 <= nums[i] < n
# nums 中的所有整数 互不相同
# nums 是范围 [0, n - 1] 内所有数字组成的一个排列
#
#
#
from typing import List


# @lc code=start
class Solution:

    def isIdealPermutation(self, nums: List[int]) -> bool:
        min_value = nums[-1]
        for i in range(len(nums) - 3, -1, -1):
            min_value = min(min_value, nums[i + 2])
            if nums[i] > min_value:
                return False
        return True


# @lc code=end

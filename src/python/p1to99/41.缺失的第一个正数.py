#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   41.缺失的第一个正数.py
@Time    :   2020/10/30 21:56:02
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode-cn.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (40.31%)
# Likes:    834
# Dislikes: 0
# Total Accepted:    96.2K
# Total Submissions: 238.5K
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
#
#
#
# 示例 1:
#
# 输入: [1,2,0]
# 输出: 3
#
#
# 示例 2:
#
# 输入: [3,4,-1,1]
# 输出: 2
#
#
# 示例 3:
#
# 输入: [7,8,9,11,12]
# 输出: 1
#
#
#
#
# 提示：
#
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
#
#
from typing import List


# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1


# @lc code=end

# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         if not nums:
#             return 1

#         n = len(nums)
#         for i in range(n):
#             while (nums[i] > 0 and nums[i] <= n
#                    and nums[nums[i] - 1] != nums[i]):
#                 to = nums[i]
#                 nums[i], nums[to - 1] = nums[to - 1], nums[i]

#         for i in range(n):
#             if nums[i] != i + 1:
#                 return i + 1

#         return n + 1

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   915.分割数组.py
@Time    :   2022/10/24 21:30:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=915 lang=python3
#
# [915] 分割数组
#
# https://leetcode.cn/problems/partition-array-into-disjoint-intervals/description/
#
# algorithms
# Medium (47.26%)
# Likes:    205
# Dislikes: 0
# Total Accepted:    39.2K
# Total Submissions: 78.5K
# Testcase Example:  '[5,0,3,8,6]'
#
# 给定一个数组 nums ，将其划分为两个连续子数组 left 和 right， 使得：
#
#
# left 中的每个元素都小于或等于 right 中的每个元素。
# left 和 right 都是非空的。
# left 的长度要尽可能小。
#
#
# 在完成这样的分组后返回 left 的 长度 。
#
# 用例可以保证存在这样的划分方法。
#
#
#
# 示例 1：
#
#
# 输入：nums = [5,0,3,8,6]
# 输出：3
# 解释：left = [5,0,3]，right = [8,6]
#
#
# 示例 2：
#
#
# 输入：nums = [1,1,1,0,6,12]
# 输出：4
# 解释：left = [1,1,1,0]，right = [6,12]
#
#
#
#
# 提示：
#
#
# 2 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^6
# 可以保证至少有一种方法能够按题目所描述的那样对 nums 进行划分。
#
#
#
from typing import List


# @lc code=start
class Solution:

    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = cur_max = nums[0]
        left_pos, n = 0, len(nums)
        for i in range(1, n - 1):
            cur_max = max(cur_max, nums[i])
            if nums[i] < left_max:
                left_max, left_pos = cur_max, i
        return left_pos + 1


# @lc code=end

# class Solution:

#     def partitionDisjoint(self, nums: List[int]) -> int:
#         n = len(nums)
#         maxs = [-0x80000000] * n
#         mins = [0x7FFFFFFF] * n

#         maxs[0], mins[-1] = nums[0], nums[-1]

#         for i in range(1, n):
#             maxs[i] = max(maxs[i - 1], nums[i])
#             mins[n - i - 1] = min(mins[n - i], nums[n - i - 1])

#         for i in range(n - 1):
#             if maxs[i] <= mins[i + 1]:
#                 return i + 1

#         return -1

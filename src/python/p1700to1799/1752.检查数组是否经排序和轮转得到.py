#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1752.检查数组是否经排序和轮转得到.py
@Time    :   2022/11/27 11:47:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=1752 lang=python3
#
# [1752] 检查数组是否经排序和轮转得到
#
# https://leetcode.cn/problems/check-if-array-is-sorted-and-rotated/description/
#
# algorithms
# Easy (61.55%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    19.2K
# Total Submissions: 31.8K
# Testcase Example:  '[3,4,5,1,2]'
#
# 给你一个数组 nums 。nums 的源数组中，所有元素与 nums 相同，但按非递减顺序排列。
#
# 如果 nums 能够由源数组轮转若干位置（包括 0 个位置）得到，则返回 true ；否则，返回 false 。
#
# 源数组中可能存在 重复项 。
#
# 注意：我们称数组 A 在轮转 x 个位置后得到长度相同的数组 B ，当它们满足 A[i] == B[(i+x) % A.length] ，其中 %
# 为取余运算。
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,4,5,1,2]
# 输出：true
# 解释：[1,2,3,4,5] 为有序的源数组。
# 可以轮转 x = 3 个位置，使新数组从值为 3 的元素开始：[3,4,5,1,2] 。
#
#
# 示例 2：
#
#
# 输入：nums = [2,1,3,4]
# 输出：false
# 解释：源数组无法经轮转得到 nums 。
#
#
# 示例 3：
#
#
# 输入：nums = [1,2,3]
# 输出：true
# 解释：[1,2,3] 为有序的源数组。
# 可以轮转 x = 0 个位置（即不轮转）得到 nums 。
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
#
#
#
from typing import List


# @lc code=start
class Solution:

    def check(self, nums: List[int]) -> bool:
        i, n = 1, len(nums)
        while i < n and nums[i] >= nums[i - 1]:
            i += 1

        if i == n:
            return True

        def is_ordered(start: int, end: int) -> bool:
            while start < end and nums[start] <= nums[start + 1]:
                start += 1
            return start == end

        return (nums[0] >= nums[-1] and is_ordered(0, i - 1)
                and is_ordered(i, n - 1))


# @lc code=end

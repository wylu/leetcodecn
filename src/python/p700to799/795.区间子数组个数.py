#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   795.区间子数组个数.py
@Time    :   2022/11/24 17:36:47
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=795 lang=python3
#
# [795] 区间子数组个数
#
# https://leetcode.cn/problems/number-of-subarrays-with-bounded-maximum/description/
#
# algorithms
# Medium (53.04%)
# Likes:    287
# Dislikes: 0
# Total Accepted:    25.8K
# Total Submissions: 45.6K
# Testcase Example:  '[2,1,4,3]\n2\n3'
#
# 给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围 [left, right]
# 内的子数组，并返回满足条件的子数组的个数。
#
# 生成的测试用例保证结果符合 32-bit 整数范围。
#
#
#
# 示例 1：
#
#
# 输入：nums = [2,1,4,3], left = 2, right = 3
# 输出：3
# 解释：满足条件的三个子数组：[2], [2, 1], [3]
#
#
# 示例 2：
#
#
# 输入：nums = [2,9,2,5,6], left = 2, right = 8
# 输出：7
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 0 <= left <= right <= 10^9
#
#
#
from typing import List


# @lc code=start
class Solution:

    def numSubarrayBoundedMax(self, nums: List[int], left: int,
                              right: int) -> int:
        ans, i0, i1 = 0, -1, -1
        for i, num in enumerate(nums):
            if num > right:
                i0 = i
            if num >= left:
                i1 = i
            ans += i1 - i0

        return ans


# @lc code=end

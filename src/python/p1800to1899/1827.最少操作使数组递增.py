#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1827.最少操作使数组递增.py
@Time    :   2022/12/11 12:51:49
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=1827 lang=python3
#
# [1827] 最少操作使数组递增
#
# https://leetcode.cn/problems/minimum-operations-to-make-the-array-increasing/description/
#
# algorithms
# Easy (77.26%)
# Likes:    43
# Dislikes: 0
# Total Accepted:    24.9K
# Total Submissions: 31K
# Testcase Example:  '[1,1,1]'
#
# 给你一个整数数组 nums （下标从 0 开始）。每一次操作中，你可以选择数组中一个元素，并将它增加 1 。
#
#
# 比方说，如果 nums = [1,2,3] ，你可以选择增加 nums[1] 得到 nums = [1,3,3] 。
#
#
# 请你返回使 nums 严格递增 的 最少 操作次数。
#
# 我们称数组 nums 是 严格递增的 ，当它满足对于所有的 0 <= i < nums.length - 1 都有 nums[i] < nums[i+1]
# 。一个长度为 1 的数组是严格递增的一种特殊情况。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,1]
# 输出：3
# 解释：你可以进行如下操作：
# 1) 增加 nums[2] ，数组变为 [1,1,2] 。
# 2) 增加 nums[1] ，数组变为 [1,2,2] 。
# 3) 增加 nums[2] ，数组变为 [1,2,3] 。
#
#
# 示例 2：
#
# 输入：nums = [1,5,2,4,1]
# 输出：14
#
#
# 示例 3：
#
# 输入：nums = [8]
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 5000
# 1 <= nums[i] <= 10^4
#
#
#
from typing import List


# @lc code=start
class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans, cur = 0, nums[0] - 1
        for num in nums:
            if num <= cur:
                cur += 1
                ans += cur - num
            else:
                cur = num
        return ans


# @lc code=end

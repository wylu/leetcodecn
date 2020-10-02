#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   283.移动零.py
@Time    :   2020/10/02 22:52:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (62.41%)
# Likes:    750
# Dislikes: 0
# Total Accepted:    216.1K
# Total Submissions: 346.3K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
# 说明:
#
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
#
#
#
from typing import List


# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, n = 0, 0, len(nums)
        while j < n:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1


# @lc code=end

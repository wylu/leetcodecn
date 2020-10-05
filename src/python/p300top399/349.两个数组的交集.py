#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   349.两个数组的交集.py
@Time    :   2020/10/05 11:09:56
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (70.84%)
# Likes:    236
# Dislikes: 0
# Total Accepted:    96.5K
# Total Submissions: 136.2K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
#
#
# 示例 2：
#
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
#
#
#
# 说明：
#
#
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。
#
#
#
from typing import List


# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums1 = set(nums1)
        return list(set(num for num in nums2 if num in nums1))


# @lc code=end

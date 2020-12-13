#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   217.存在重复元素.py
@Time    :   2020/12/13 21:55:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
# https://leetcode-cn.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (53.41%)
# Likes:    342
# Dislikes: 0
# Total Accepted:    211.1K
# Total Submissions: 386.6K
# Testcase Example:  '[1,2,3,1]'
#
# 给定一个整数数组，判断是否存在重复元素。
#
# 如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
#
#
#
# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: true
#
# 示例 2:
#
# 输入: [1,2,3,4]
# 输出: false
#
# 示例 3:
#
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true
#
#
from typing import List


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# @lc code=end

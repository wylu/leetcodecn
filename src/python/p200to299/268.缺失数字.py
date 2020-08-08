#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   268.缺失数字.py
@Time    :   2020/08/07 23:07:04
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#
# https://leetcode-cn.com/problems/missing-number/description/
#
# algorithms
# Easy (56.54%)
# Likes:    299
# Dislikes: 0
# Total Accepted:    78.5K
# Total Submissions: 138.8K
# Testcase Example:  '[3,0,1]'
#
# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
#
#
#
# 示例 1:
#
# 输入: [3,0,1]
# 输出: 2
#
#
# 示例 2:
#
# 输入: [9,6,4,2,3,5,7,0,1]
# 输出: 8
#
#
#
#
# 说明:
# 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
#
#
from typing import List


# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (1 + n) * n // 2 - sum(nums)


# @lc code=end

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   485.最大连续-1-的个数.py
@Time    :   2020/10/02 17:06:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#
# https://leetcode-cn.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (56.78%)
# Likes:    127
# Dislikes: 0
# Total Accepted:    55.4K
# Total Submissions: 97.5K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# 给定一个二进制数组， 计算其中最大连续1的个数。
#
# 示例 1:
#
#
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
#
#
# 注意：
#
#
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。
#
#
#
from typing import List


# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, cnt = 0, 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
        return max(ans, cnt)


# @lc code=end

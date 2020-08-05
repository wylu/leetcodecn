#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   66.加一.py
@Time    :   2020/08/05 22:58:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (44.94%)
# Likes:    521
# Dislikes: 0
# Total Accepted:    184.5K
# Total Submissions: 410.5K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#
#
# 示例 2:
#
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#
#
#
from typing import List


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            carry += digits[i]
            ans.append(carry % 10)
            carry //= 10

        if carry > 0:
            ans.append(carry)

        ans.reverse()
        return ans


# @lc code=end

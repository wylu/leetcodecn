#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   728.自除数.py
@Time    :   2022/03/31 20:41:01
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#
# https://leetcode-cn.com/problems/self-dividing-numbers/description/
#
# algorithms
# Easy (78.61%)
# Likes:    216
# Dislikes: 0
# Total Accepted:    63.4K
# Total Submissions: 80.7K
# Testcase Example:  '1\n22'
#
# 自除数 是指可以被它包含的每一位数整除的数。
#
#
# 例如，128 是一个 自除数 ，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
#
#
# 自除数 不允许包含 0 。
#
# 给定两个整数 left 和 right ，返回一个列表，列表的元素是范围 [left, right] 内所有的 自除数 。
#
#
#
# 示例 1：
#
#
# 输入：left = 1, right = 22
# 输出：[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
#
#
# 示例 2:
#
#
# 输入：left = 47, right = 85
# 输出：[48,55,66,77]
#
#
#
#
# 提示：
#
#
# 1 <= left <= right <= 10^4
#
#
#
from typing import List


# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right + 1):
            i, flag = num, True
            while i:
                i, r = divmod(i, 10)
                if not r or num % r:
                    flag = False
                    break

            if flag:
                ans.append(num)

        return ans


# @lc code=end

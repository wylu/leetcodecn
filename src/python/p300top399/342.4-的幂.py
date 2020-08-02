#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   342.4-的幂.py
@Time    :   2020/08/02 23:39:09
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#
# https://leetcode-cn.com/problems/power-of-four/description/
#
# algorithms
# Easy (49.00%)
# Likes:    125
# Dislikes: 0
# Total Accepted:    28.7K
# Total Submissions: 58.5K
# Testcase Example:  '16'
#
# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
#
# 示例 1:
#
# 输入: 16
# 输出: true
#
#
# 示例 2:
#
# 输入: 5
# 输出: false
#
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
#
#
"""
我们首先检车 x 是否为 2 的幂：x > 0 and x & (x - 1) == 0。
然后可以确定 x = 2^a，若 x 为 4 的幂则 a 为偶数。

下一步是考虑 a = 2k 和 a = 2k+1 两种情况，对 x 对 3 进行取模：

(2^(2k) mod 3) = (4^k mod 3) = ((3+1)^k mod 3) = 1
(2^(2k+1) mod 3) = ((2*4^k) mod 3) = ((2*(3+1)^k) mod 3) = 2

若 x 为 2 的幂且 x%3 == 1，则 x 为 4 的幂。
"""


# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1


# @lc code=end

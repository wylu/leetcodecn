#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   461.汉明距离.py
@Time    :   2020/08/07 21:53:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#
# https://leetcode-cn.com/problems/hamming-distance/description/
#
# algorithms
# Easy (77.08%)
# Likes:    306
# Dislikes: 0
# Total Accepted:    66.2K
# Total Submissions: 85.9K
# Testcase Example:  '1\n4'
#
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
#
# 注意：
# 0 ≤ x, y < 2^31.
#
# 示例:
#
#
# 输入: x = 1, y = 4
#
# 输出: 2
#
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
#
# 上面的箭头指出了对应二进制位不同的位置。
#
#
#


# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        z = x ^ y
        while z:
            z &= (z - 1)
            ans += 1
        return ans


# @lc code=end

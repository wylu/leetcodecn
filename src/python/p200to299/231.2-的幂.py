#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   231.2-的幂.py
@Time    :   2020/08/02 23:13:09
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (48.29%)
# Likes:    225
# Dislikes: 0
# Total Accepted:    70.8K
# Total Submissions: 146.4K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#
# 示例 1:
#
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
#
# 示例 2:
#
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
#
# 示例 3:
#
# 输入: 218
# 输出: false
#
#
"""
该问题将通过位运算可在 O(1) 的时间复杂度解决，通过使用如下的按位技巧：

  - 如何获取二进制中最右边的 1：x & (-x)
  - 如何将二进制中最右边的 1 设置为 0：x & (x - 1)

以下的两种解决方案背后的思想都是一样的：
2 的幂在二进制中是有一个 1 后跟一些 0：

1 = 0000 0001
2 = 0000 0010
4 = 0000 0100
8 = 0000 1000

不是 2 的幂的二进制中有一个以上的 1

3 = 0000 0011
5 = 0000 0101
6 = 0000 0110
7 = 0000 0111
"""


# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0


# @lc code=end

# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0:
#             return False

#         cnt = 0
#         while n != 0:
#             cnt += (n & 1)
#             n >>= 1

#         return cnt == 1

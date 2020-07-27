#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   7.整数反转.py
@Time    :   2020/07/27 22:02:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (34.47%)
# Likes:    2063
# Dislikes: 0
# Total Accepted:    415.3K
# Total Submissions: 1.2M
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#
#
# 示例 2:
#
# 输入: -123
# 输出: -321
#
#
# 示例 3:
#
# 输入: 120
# 输出: 21
#
#
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
#
#


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT32, MIN_INT32 = 0x7FFFFFFF, -0x80000000
        sign = 1 if x >= 0 else -1
        x, ans = abs(x), 0

        while x != 0:
            pop = x % 10
            x //= 10

            if ans > MAX_INT32 // 10 or (ans == MAX_INT32 and pop > 7):
                return 0
            if ans < MIN_INT32 // 10 or (ans == MIN_INT32 and pop < -8):
                return 0

            ans = ans * 10 + pop

        return sign * ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.reverse(-123))

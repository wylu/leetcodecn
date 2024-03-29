#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   788.旋转数字.py
@Time    :   2022/09/25 15:23:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#
# https://leetcode.cn/problems/rotated-digits/description/
#
# algorithms
# Medium (61.49%)
# Likes:    153
# Dislikes: 0
# Total Accepted:    31.9K
# Total Submissions: 49.2K
# Testcase Example:  '10'
#
# 我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。
#
# 如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5
# 可以互相旋转成对方（在这种情况下，它们以不同的方向旋转，换句话说，2 和 5 互为镜像）；6 和 9
# 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。
#
# 现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？
#
#
#
# 示例：
#
# 输入: 10
# 输出: 4
# 解释:
# 在[1, 10]中有四个好数： 2, 5, 6, 9。
# 注意 1 和 10 不是好数, 因为他们在旋转之后不变。
#
#
#
#
# 提示：
#
#
# N 的取值范围是 [1, 10000]。
#
#
#


# @lc code=start
class Solution:

    def rotatedDigits(self, n: int) -> int:
        DIFFS = (0, 0, 1, -1, -1, 1, 1, -1, 0, 1)
        s = str(n)

        def f(i: int, has_diff: bool, is_limit: bool) -> int:
            if i == len(s):
                return int(has_diff)

            res = 0
            up = int(s[i]) if is_limit else 9
            for d in range(0, up + 1):
                if DIFFS[d] != -1:
                    res += f(i + 1, has_diff or DIFFS[d], is_limit and d == up)

            return res

        return f(0, False, True)


# @lc code=end

# class Solution:

#     def rotatedDigits(self, n: int) -> int:
#         ans = 0
#         a, b = set(list('0182569')), set(list('2569'))
#         for num in range(1, n + 1):
#             s = set(list(str(num)))
#             if s.issubset(a) and s & b:
#                 ans += 1
#         return ans

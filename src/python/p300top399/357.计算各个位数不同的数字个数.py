#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   357.计算各个位数不同的数字个数.py
@Time    :   2021/04/19 22:30:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 计算各个位数不同的数字个数
#
# https://leetcode-cn.com/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (51.38%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    21K
# Total Submissions: 40.9K
# Testcase Example:  '2'
#
# 给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10^n 。
#
# 示例:
#
# 输入: 2
# 输出: 91
# 解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
#
#
#


# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = 1
        for i in range(min(n, 10)):
            base, delta = 9, 9
            for _ in range(i):
                base *= delta
                delta -= 1
            ans += base
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.countNumbersWithUniqueDigits(0))
    print(solu.countNumbersWithUniqueDigits(1))
    print(solu.countNumbersWithUniqueDigits(2))
    print(solu.countNumbersWithUniqueDigits(3))

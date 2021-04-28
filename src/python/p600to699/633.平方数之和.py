#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   633.平方数之和.py
@Time    :   2021/04/28 22:25:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#
# https://leetcode-cn.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Medium (39.49%)
# Likes:    261
# Dislikes: 0
# Total Accepted:    76.6K
# Total Submissions: 194.1K
# Testcase Example:  '5'
#
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c 。
#
#
#
# 示例 1：
#
# 输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5
#
#
# 示例 2：
#
# 输入：c = 3
# 输出：false
#
#
# 示例 3：
#
# 输入：c = 4
# 输出：true
#
#
# 示例 4：
#
# 输入：c = 2
# 输出：true
#
#
# 示例 5：
#
# 输入：c = 1
# 输出：true
#
#
#
# 提示：
#
#
# 0 <= c <= 2^31 - 1
#
#
#
import math


# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c)) + 1):
            b = math.sqrt(c - a * a)
            if b == int(b):
                return True
        return False


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.judgeSquareSum(5))
    print(solu.judgeSquareSum(3))
    print(solu.judgeSquareSum(4))
    print(solu.judgeSquareSum(2))
    print(solu.judgeSquareSum(1))
    print(solu.judgeSquareSum(0))
    print(solu.judgeSquareSum(0x7FFFFFFF))
    print(solu.judgeSquareSum(256**2 + 1024**2))
    print(solu.judgeSquareSum(32))

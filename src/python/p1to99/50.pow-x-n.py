#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   50.pow-x-n.py
@Time    :   2020/10/04 23:07:47
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode-cn.com/problems/powx-n/description/
#
# algorithms
# Medium (36.73%)
# Likes:    506
# Dislikes: 0
# Total Accepted:    130.4K
# Total Submissions: 355K
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
# 示例 1:
#
# 输入: 2.00000, 10
# 输出: 1024.00000
#
#
# 示例 2:
#
# 输入: 2.10000, 3
# 输出: 9.26100
#
#
# 示例 3:
#
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2^-2 = 1/2^2 = 1/4 = 0.25
#
# 说明:
#
#
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
#
#
#


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x

        ans = 1
        while n > 0:
            if n & 1 == 1:
                ans = ans * x
            x *= x
            n >>= 1
        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.myPow(2.00000, 10))
    print(solu.myPow(2.10000, 3))
    print(solu.myPow(2.00000, -2))

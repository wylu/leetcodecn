#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   509.斐波那契数.py
@Time    :   2021/01/04 09:01:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#
# https://leetcode-cn.com/problems/fibonacci-number/description/
#
# algorithms
# Easy (66.21%)
# Likes:    195
# Dislikes: 0
# Total Accepted:    102.7K
# Total Submissions: 154.4K
# Testcase Example:  '2'
#
# 斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
#
#
# F(0) = 0，F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
#
#
# 给你 n ，请计算 F(n) 。
#
#
#
# 示例 1：
#
#
# 输入：2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1
#
#
# 示例 2：
#
#
# 输入：3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2
#
#
# 示例 3：
#
#
# 输入：4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3
#
#
#
#
# 提示：
#
#
# 0 ≤ n ≤ 30
#
#
#


# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1]
        if n < 2:
            return f[n]

        for i in range(2, n + 1):
            f[0], f[1] = f[1], f[0] + f[1]
        return f[1]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.fib(0))
    print(solu.fib(1))
    print(solu.fib(2))
    print(solu.fib(3))
    print(solu.fib(30))

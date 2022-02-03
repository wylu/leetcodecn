#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1414.和为-k-的最少斐波那契数字数目.py
@Time    :   2022/02/03 09:54:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1414 lang=python3
#
# [1414] 和为 K 的最少斐波那契数字数目
#
# https://leetcode-cn.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/description/
#
# algorithms
# Medium (64.57%)
# Likes:    72
# Dislikes: 0
# Total Accepted:    10.7K
# Total Submissions: 16.6K
# Testcase Example:  '7'
#
# 给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。
#
# 斐波那契数字定义为：
#
#
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 ， 其中 n > 2 。
#
#
# 数据保证对于给定的 k ，一定能找到可行解。
#
#
#
# 示例 1：
#
# 输入：k = 7
# 输出：2
# 解释：斐波那契数字为：1，1，2，3，5，8，13，……
# 对于 k = 7 ，我们可以得到 2 + 5 = 7 。
#
# 示例 2：
#
# 输入：k = 10
# 输出：2
# 解释：对于 k = 10 ，我们可以得到 2 + 8 = 10 。
#
#
# 示例 3：
#
# 输入：k = 19
# 输出：3
# 解释：对于 k = 19 ，我们可以得到 1 + 5 + 13 = 19 。
#
#
#
#
# 提示：
#
#
# 1 <= k <= 10^9
#
#
#


# @lc code=start
class Solution:

    def findMinFibonacciNumbers(self, k: int) -> int:
        f = [0, 1, 1]
        while f[-1] < k:
            f.append(f[-2] + f[-1])

        ans = 0
        while k:
            if k >= f[-1]:
                k -= f[-1]
                ans += 1

            f.pop()

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.findMinFibonacciNumbers(7))
    print(solu.findMinFibonacciNumbers(10))
    print(solu.findMinFibonacciNumbers(19))

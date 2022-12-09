#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1780.判断一个数字是否可以表示成三的幂的和.py
@Time    :   2022/12/09 09:27:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1780 lang=python3
#
# [1780] 判断一个数字是否可以表示成三的幂的和
#
# https://leetcode.cn/problems/check-if-number-is-a-sum-of-powers-of-three/description/
#
# algorithms
# Medium (67.36%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    12.2K
# Total Submissions: 17K
# Testcase Example:  '12'
#
# 给你一个整数 n ，如果你可以将 n 表示成若干个不同的三的幂之和，请你返回 true ，否则请返回 false 。
#
# 对于一个整数 y ，如果存在整数 x 满足 y == 3^x ，我们称这个整数 y 是三的幂。
#
#
#
# 示例 1：
#
# 输入：n = 12
# 输出：true
# 解释：12 = 3^1 + 3^2
#
#
# 示例 2：
#
# 输入：n = 91
# 输出：true
# 解释：91 = 3^0 + 3^2 + 3^4
#
#
# 示例 3：
#
# 输入：n = 21
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= n <= 10^7
#
#
#


# @lc code=start
class Solution:

    def checkPowersOfThree(self, n: int) -> bool:
        while n and n % 3 != 2:
            n //= 3
        return n == 0


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.checkPowersOfThree(12))
    print(solu.checkPowersOfThree(91))
    print(solu.checkPowersOfThree(21))

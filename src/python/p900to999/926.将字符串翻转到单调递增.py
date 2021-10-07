#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   926.将字符串翻转到单调递增.py
@Time    :   2021/10/07 14:11:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=926 lang=python3
#
# [926] 将字符串翻转到单调递增
#
# https://leetcode-cn.com/problems/flip-string-to-monotone-increasing/description/
#
# algorithms
# Medium (52.18%)
# Likes:    111
# Dislikes: 0
# Total Accepted:    6.7K
# Total Submissions: 12.9K
# Testcase Example:  '"00110"'
#
# 如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有
# '1'）的形式组成的，那么该字符串是单调递增的。
#
# 我们给出一个由字符 '0' 和 '1' 组成的字符串 S，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。
#
# 返回使 S 单调递增的最小翻转次数。
#
#
#
# 示例 1：
#
#
# 输入："00110"
# 输出：1
# 解释：我们翻转最后一位得到 00111.
#
#
# 示例 2：
#
#
# 输入："010110"
# 输出：2
# 解释：我们翻转得到 011111，或者是 000111。
#
#
# 示例 3：
#
#
# 输入："00011000"
# 输出：2
# 解释：我们翻转得到 00000000。
#
#
#
#
# 提示：
#
#
# 1 <= S.length <= 20000
# S 中只包含字符 '0' 和 '1'
#
#
#


# @lc code=start
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        c0, c1 = [0] * (n + 1), [0] * (n + 1)

        for i in range(n):
            c0[i + 1] = c0[i]
            if s[i] == '0':
                c0[i + 1] += 1

        for i in range(n - 1, -1, -1):
            c1[i] = c1[i + 1]
            if s[i] == '1':
                c1[i] += 1

        ans = 0x7FFFFFFF
        for i in range(n + 1):
            a = i - c0[i]  # convert 1 to 0
            b = (n - i) - c1[i]  # convert 0 to 1
            ans = min(ans, a + b)

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.minFlipsMonoIncr("00110"))
    print(solu.minFlipsMonoIncr("010110"))
    print(solu.minFlipsMonoIncr("00011000"))

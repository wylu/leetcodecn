#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   899.有序队列.py
@Time    :   2022/08/03 14:34:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=899 lang=python3
#
# [899] 有序队列
#
# https://leetcode.cn/problems/orderly-queue/description/
#
# algorithms
# Hard (63.20%)
# Likes:    112
# Dislikes: 0
# Total Accepted:    15.2K
# Total Submissions: 24.1K
# Testcase Example:  '"cba"\n1'
#
# 给定一个字符串 s 和一个整数 k 。你可以从 s 的前 k 个字母中选择一个，并把它加到字符串的末尾。
#
# 返回 在应用上述步骤的任意数量的移动后，字典上最小的字符串 。
#
#
#
# 示例 1：
#
#
# 输入：s = "cba", k = 1
# 输出："acb"
# 解释：
# 在第一步中，我们将第一个字符（“c”）移动到最后，获得字符串 “bac”。
# 在第二步中，我们将第一个字符（“b”）移动到最后，获得最终结果 “acb”。
#
#
# 示例 2：
#
#
# 输入：s = "baaca", k = 3
# 输出："aaabc"
# 解释：
# 在第一步中，我们将第一个字符（“b”）移动到最后，获得字符串 “aacab”。
# 在第二步中，我们将第三个字符（“c”）移动到最后，获得最终结果 “aaabc”。
#
#
#
#
# 提示：
#
#
# 1 <= k <= S.length <= 1000
# s 只由小写字母组成。
#
#
#


# @lc code=start
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s
            for _ in range(len(s) - 1):
                s = s[1:] + s[0]
                ans = min(ans, s)
            return ans
        return ''.join(sorted(s))


# @lc code=end

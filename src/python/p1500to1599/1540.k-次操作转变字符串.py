#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1540.k-次操作转变字符串.py
@Time    :   2020/08/10 22:01:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1540 lang=python3
#
# [1540] K 次操作转变字符串
#
# https://leetcode-cn.com/problems/can-convert-string-in-k-moves/description/
#
# algorithms
# Medium (26.40%)
# Likes:    0
# Dislikes: 0
# Total Accepted:    2K
# Total Submissions: 7.5K
# Testcase Example:  '"input"\n"ouput"\n9'
#
# 给你两个字符串 s 和 t ，你的目标是在 k 次操作以内把字符串 s 转变成 t 。
#
# 在第 i 次操作时（1 <= i <= k），你可以选择进行如下操作：
#
#
# 选择字符串 s 中满足 1 <= j <= s.length 且之前未被选过的任意下标 j （下标从 1 开始），并将此位置的字符切换 i 次。
# 不进行任何操作。
#
#
# 切换 1 次字符的意思是用字母表中该字母的下一个字母替换它（字母表环状接起来，所以 'z' 切换后会变成 'a'）。
#
# 请记住任意一个下标 j 最多只能被操作 1 次。
#
# 如果在不超过 k 次操作内可以把字符串 s 转变成 t ，那么请你返回 true ，否则请你返回 false 。
#
#
#
# 示例 1：
#
# 输入：s = "input", t = "ouput", k = 9
# 输出：true
# 解释：第 6 次操作时，我们将 'i' 切换 6 次得到 'o' 。第 7 次操作时，我们将 'n' 切换 7 次得到 'u' 。
#
#
# 示例 2：
#
# 输入：s = "abc", t = "bcd", k = 10
# 输出：false
# 解释：我们需要将每个字符切换 1 次才能得到 t 。我们可以在第 1 次操作时将 'a' 切换成 'b' ，但另外 2 个字母在剩余操作中无法再转变为 t
# 中对应字母。
#
#
# 示例 3：
#
# 输入：s = "aab", t = "bbb", k = 27
# 输出：true
# 解释：第 1 次操作时，我们将第一个 'a' 切换 1 次得到 'b' 。在第 27 次操作时，我们将第二个字母 'a' 切换 27 次得到 'b'
# 。
#
#
#
#
# 提示：
#
#
# 1 <= s.length, t.length <= 10^5
# 0 <= k <= 10^9
# s 和 t 只包含小写英文字母。
#
#
#
"""
方法一：统计操作次数

由于每次操作只是切换字符串中的字符，不会改变字符串的长度，因此只有当字符串 s 和 t
的长度相等时，才可能将 s 转变成 t。如果 s 和 t 的长度不相等，直接返回 false 即可。

对于每个下标，如果 s 和 t 在该下标位置的字符不相同，则需要进行切换，所需最小切换
次数最多为 25。因此，遍历 s 和 t，计算每个下标的最小切换次数（如果不需要切换，
则最小切换次数为 0），并统计每个最小切换次数的出现次数。

由于每次操作只能对一个未选过的下标位置的字符进行切换，因此如果有两个下标的最小切换
次数相同，则如果其中的一个下标在第 i 次操作时进行了切换，另一个下标必须等到第 i+26
次操作时才能进行切换。如果有多个下标的最小切换次数相同，则每个下标都必须在前一个
下标进行切换操作之后的第 26 次操作才能进行切换。

如果有 j 个下标的最小切换次数都是 i，其中 1 <= i <= 25，则需要 i + 26*(j−1) 次
操作才能将 j 个下标的字符都切换。如果 i + 26*(j−1) > k，则无法在 k 次操作以内
完成全部的切换操作，因此返回 false。

如果对于所有的最小切换次数，所有的下标都可以在 k 次操作以内进行切换，则返回 true。
"""


# @lc code=start
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        cnt = [0] * 26
        for i in range(len(s)):
            delta = (ord(t[i]) - ord(s[i]) + 26) % 26
            cnt[delta] += 1

        hi = 0
        for i in range(1, 26):
            hi = max(hi, i + (cnt[i] - 1) * 26)

        return hi <= k


# @lc code=end

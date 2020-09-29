#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1513.仅含-1-的子串数.py
@Time    :   2020/09/29 19:07:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1513 lang=python3
#
# [1513] 仅含 1 的子串数
#
# https://leetcode-cn.com/problems/number-of-substrings-with-only-1s/description/
#
# algorithms
# Medium (36.27%)
# Likes:    9
# Dislikes: 0
# Total Accepted:    7.7K
# Total Submissions: 21.3K
# Testcase Example:  '"0110111"'
#
# 给你一个二进制字符串 s（仅由 '0' 和 '1' 组成的字符串）。
#
# 返回所有字符都为 1 的子字符串的数目。
#
# 由于答案可能很大，请你将它对 10^9 + 7 取模后返回。
#
#
#
# 示例 1：
#
# 输入：s = "0110111"
# 输出：9
# 解释：共有 9 个子字符串仅由 '1' 组成
# "1" -> 5 次
# "11" -> 3 次
# "111" -> 1 次
#
# 示例 2：
#
# 输入：s = "101"
# 输出：2
# 解释：子字符串 "1" 在 s 中共出现 2 次
#
#
# 示例 3：
#
# 输入：s = "111111"
# 输出：21
# 解释：每个子字符串都仅由 '1' 组成
#
#
# 示例 4：
#
# 输入：s = "000"
# 输出：0
#
#
#
#
# 提示：
#
#
# s[i] == '0' 或 s[i] == '1'
# 1 <= s.length <= 10^5
#
#
#


# @lc code=start
class Solution:
    def numSub(self, s: str) -> int:
        ans, cnt = 0, 0
        for ch in s:
            if ch == '0':
                ans += (1 + cnt) * cnt // 2
                cnt = 0
            else:
                cnt += 1

        ans += (1 + cnt) * cnt // 2
        return ans % (10**9 + 7)


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.numSub('0110111'))
    print(solu.numSub('101'))
    # 6 + 5 + 4 + 3 + 2 + 1 = (1 + 6) * 6 / 2 = 21
    print(solu.numSub('111111'))
    print(solu.numSub('000'))

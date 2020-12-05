#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   3.无重复字符的最长子串.py
@Time    :   2020/12/05 22:43:13
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (35.94%)
# Likes:    4665
# Dislikes: 0
# Total Accepted:    748.7K
# Total Submissions: 2.1M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
#
#
# 示例 1:
#
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
#
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
# 示例 4:
#
#
# 输入: s = ""
# 输出: 0
#
#
#
#
# 提示：
#
#
# 0
# s 由英文字母、数字、符号和空格组成
#
#
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        ans, i, j, n = 0, 0, 0, len(s)
        seen = set()

        while n - i > ans:
            while j < n and s[j] not in seen:
                seen.add(s[j])
                j += 1
            ans = max(ans, j - i)
            seen.remove(s[i])
            i += 1

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.lengthOfLongestSubstring("abcabcbb"))
    print(solu.lengthOfLongestSubstring("bbbbb"))
    print(solu.lengthOfLongestSubstring("pwwkew"))

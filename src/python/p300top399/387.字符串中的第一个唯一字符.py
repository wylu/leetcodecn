#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   387.字符串中的第一个唯一字符.py
@Time    :   2020/12/23 17:54:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (50.42%)
# Likes:    332
# Dislikes: 0
# Total Accepted:    140.6K
# Total Submissions: 278.9K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
#
#
# 示例：
#
# s = "leetcode"
# 返回 0
#
# s = "loveleetcode"
# 返回 2
#
#
#
#
# 提示：你可以假定该字符串只包含小写字母。
#
#
from collections import defaultdict


# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnts = defaultdict(int)
        for ch in s:
            cnts[ch] += 1

        for i, ch in enumerate(s):
            if cnts[ch] == 1:
                return i

        return -1


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.firstUniqChar("leetcode"))
    print(solu.firstUniqChar("loveleetcode"))

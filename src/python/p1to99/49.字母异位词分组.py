#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   49.字母异位词分组.py
@Time    :   2020/10/12 13:45:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (63.81%)
# Likes:    487
# Dislikes: 0
# Total Accepted:    111.9K
# Total Submissions: 175.3K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
#
# 说明：
#
#
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
#
#
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for s in strs:
            t = ''.join(sorted(list(s)))
            words[t].append(s)
        return [ss for _, ss in words.items()]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

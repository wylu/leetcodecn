#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1239.串联字符串的最大长度.py
@Time    :   2021/06/19 10:09:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1239 lang=python3
#
# [1239] 串联字符串的最大长度
#
# https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
#
# algorithms
# Medium (43.30%)
# Likes:    107
# Dislikes: 0
# Total Accepted:    18.8K
# Total Submissions: 43.5K
# Testcase Example:  '["un","iq","ue"]'
#
# 给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
#
# 请返回所有可行解 s 中最长长度。
#
#
#
# 示例 1：
#
# 输入：arr = ["un","iq","ue"]
# 输出：4
# 解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。
#
#
# 示例 2：
#
# 输入：arr = ["cha","r","act","ers"]
# 输出：6
# 解释：可能的解答有 "chaers" 和 "acters"。
#
#
# 示例 3：
#
# 输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
# 输出：26
#
#
#
#
# 提示：
#
#
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] 中只含有小写英文字母
#
#
#
from typing import List


# @lc code=start
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        for state in range(1, 1 << len(arr)):
            s, seen = [], set()
            flag = True
            while state:
                for ch in arr[len(bin(state & -state)) - 3]:
                    if ch in seen:
                        flag = False
                        break
                    s.append(ch)
                    seen.add(ch)
                if not flag:
                    break
                state &= (state - 1)
            if flag:
                ans = max(ans, len(s))
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.maxLength(["un", "iq", "ue"]))
    print(solu.maxLength(["cha", "r", "act", "ers"]))
    print(solu.maxLength(["abcdefghijklmnopqrstuvwxyz"]))

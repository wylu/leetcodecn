#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   557.反转字符串中的单词-iii.py
@Time    :   2020/08/30 00:02:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#
# https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (71.59%)
# Likes:    217
# Dislikes: 0
# Total Accepted:    73K
# Total Submissions: 102K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#
#
#
# 示例：
#
# 输入："Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
#
#
#
#
# 提示：
#
#
# 在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
#
#
#


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        return ' '.join(s)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.reverseWords("Let's take LeetCode contest"))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   500.键盘行.py
@Time    :   2021/10/31 10:17:49
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#
# https://leetcode-cn.com/problems/keyboard-row/description/
#
# algorithms
# Easy (72.44%)
# Likes:    154
# Dislikes: 0
# Total Accepted:    36.1K
# Total Submissions: 49.8K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。
#
# 美式键盘 中：
#
#
# 第一行由字符 "qwertyuiop" 组成。
# 第二行由字符 "asdfghjkl" 组成。
# 第三行由字符 "zxcvbnm" 组成。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：words = ["Hello","Alaska","Dad","Peace"]
# 输出：["Alaska","Dad"]
#
#
# 示例 2：
#
#
# 输入：words = ["omk"]
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：words = ["adsdf","sfd"]
# 输出：["adsdf","sfd"]
#
#
#
#
# 提示：
#
#
# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] 由英文字母（小写和大写字母）组成
#
#
#
from typing import List


# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        c2l = {}
        for i, line in enumerate(['qwertyuiop', 'asdfghjkl', 'zxcvbnm']):
            for ch in line:
                c2l[ch] = i

        ans = []
        for word in words:
            lno = c2l[word[0].lower()]
            for ch in word.lower():
                if c2l[ch] != lno:
                    break
            else:
                ans.append(word)

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.findWords(words=["Hello", "Alaska", "Dad", "Peace"]))
    print(solu.findWords(words=["omk"]))
    print(solu.findWords(words=["adsdf", "sfd"]))

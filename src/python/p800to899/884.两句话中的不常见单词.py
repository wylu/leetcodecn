#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   884.两句话中的不常见单词.py
@Time    :   2022/01/30 20:51:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#
# https://leetcode-cn.com/problems/uncommon-words-from-two-sentences/description/
#
# algorithms
# Easy (71.27%)
# Likes:    145
# Dislikes: 0
# Total Accepted:    36.2K
# Total Submissions: 50.9K
# Testcase Example:  '"this apple is sweet"\n"this apple is sour"'
#
# 句子 是一串由空格分隔的单词。每个 单词 仅由小写字母组成。
#
# 如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 没有出现 ，那么这个单词就是 不常见的 。
#
# 给你两个 句子 s1 和 s2 ，返回所有 不常用单词 的列表。返回列表中单词可以按 任意顺序 组织。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：s1 = "this apple is sweet", s2 = "this apple is sour"
# 输出：["sweet","sour"]
#
#
# 示例 2：
#
#
# 输入：s1 = "apple apple", s2 = "banana"
# 输出：["banana"]
#
#
#
#
# 提示：
#
#
# 1 <= s1.length, s2.length <= 200
# s1 和 s2 由小写英文字母和空格组成
# s1 和 s2 都不含前导或尾随空格
# s1 和 s2 中的所有单词间均由单个空格分隔
#
#
#
from collections import Counter
from typing import List


# @lc code=start
class Solution:

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = []
        c1, c2 = Counter(s1.split()), Counter(s2.split())

        for key, value in c1.items():
            if value == 1 and key not in c2:
                ans.append(key)

        for key, value in c2.items():
            if value == 1 and key not in c1:
                ans.append(key)

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    s1, s2 = "this apple is sweet", "this apple is sour"
    print(solu.uncommonFromSentences(s1, s2))

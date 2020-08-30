#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   345.反转字符串中的元音字母.py
@Time    :   2020/08/30 10:01:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (50.61%)
# Likes:    112
# Dislikes: 0
# Total Accepted:    45.4K
# Total Submissions: 89.8K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
#
#
# 示例 1：
#
# 输入："hello"
# 输出："holle"
#
#
# 示例 2：
#
# 输入："leetcode"
# 输出："leotcede"
#
#
#
# 提示：
#
#
# 元音字母不包含字母 "y" 。
#
#
#


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i] not in vowel:
                i += 1
            while i < j and s[j] not in vowel:
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.reverseVowels('aA'))
    print(solu.reverseVowels('leetcode'))

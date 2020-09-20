#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   394.字符串解码.py
@Time    :   2020/09/20 12:30:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
# https://leetcode-cn.com/problems/decode-string/description/
#
# algorithms
# Medium (53.15%)
# Likes:    500
# Dislikes: 0
# Total Accepted:    62.2K
# Total Submissions: 117.1K
# Testcase Example:  '"3[a]2[bc]"'
#
# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
#
#
# 示例 1：
#
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
#
#
# 示例 2：
#
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
#
#
# 示例 3：
#
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
#
#
# 示例 4：
#
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#
#
#


# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        num, cnts, vals = 0, [], [[]]
        for ch in s:
            if '0' <= ch <= '9':
                num = num * 10 + ord(ch) - ord('0')
            elif ch == '[':
                vals.append([])
                cnts.append(num)
                num = 0
            elif ch == ']':
                tmp = ''.join(vals.pop()) * cnts.pop()
                vals[-1].append(tmp)
            else:
                vals[-1].append(ch)

        return ''.join(vals[-1])


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.decodeString("3[a]2[bc]"))
    print(solu.decodeString("3[a2[c]]"))
    print(solu.decodeString("2[abc]3[cd]ef"))
    print(solu.decodeString("abc3[cd]xyz"))

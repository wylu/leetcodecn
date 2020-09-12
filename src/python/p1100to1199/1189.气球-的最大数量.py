#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1189.气球-的最大数量.py
@Time    :   2020/09/12 12:49:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] “气球” 的最大数量
#
# https://leetcode-cn.com/problems/maximum-number-of-balloons/description/
#
# algorithms
# Easy (63.55%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    13.6K
# Total Submissions: 21.4K
# Testcase Example:  '"nlaebolko"'
#
# 给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
#
# 字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。
#
#
#
# 示例 1：
#
#
#
# 输入：text = "nlaebolko"
# 输出：1
#
#
# 示例 2：
#
#
#
# 输入：text = "loonbalxballpoon"
# 输出：2
#
#
# 示例 3：
#
# 输入：text = "leetcode"
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= text.length <= 10^4
# text 全部由小写英文字母组成
#
#
#


# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnts = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for ch in text:
            if ch in cnts:
                cnts[ch] += 1
        cnts['l'] //= 2
        cnts['o'] //= 2
        return min(v for _, v in cnts.items())


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.maxNumberOfBalloons('nlaebolko'))
    print(solu.maxNumberOfBalloons('loonbalxballpoon'))
    print(solu.maxNumberOfBalloons('leetcode'))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   17.电话号码的字母组合.py
@Time    :   2020/08/26 22:35:40
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (55.29%)
# Likes:    886
# Dislikes: 0
# Total Accepted:    165.8K
# Total Submissions: 300K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#
#
from typing import List


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        def dfs(cur: int, stack: List[str]) -> None:
            if cur == len(digits):
                ans.append(''.join(stack))
                return

            for c in d2c[digits[cur]]:
                stack.append(c)
                dfs(cur + 1, stack)
                stack.pop()

        d2c = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        ans = []
        dfs(0, [])
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.letterCombinations('23'))
    print(solu.letterCombinations('9'))

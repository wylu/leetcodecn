#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   771.宝石与石头.py
@Time    :   2020/10/02 09:02:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#
# https://leetcode-cn.com/problems/jewels-and-stones/description/
#
# algorithms
# Easy (83.81%)
# Likes:    571
# Dislikes: 0
# Total Accepted:    98.4K
# Total Submissions: 117.5K
# Testcase Example:  '"aA"\n"aAAbbbb"'
#
#  给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
#
# J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。
#
# 示例 1:
#
# 输入: J = "aA", S = "aAAbbbb"
# 输出: 3
#
#
# 示例 2:
#
# 输入: J = "z", S = "ZZ"
# 输出: 0
#
#
# 注意:
#
#
# S 和 J 最多含有50个字母。
# J 中的字符不重复。
#
#
#


# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        gems = set(list(J))
        ans = 0
        for ch in S:
            if ch in gems:
                ans += 1
        return ans


# @lc code=end

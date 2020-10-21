#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   925.长按键入.py
@Time    :   2020/10/21 08:53:40
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#
# https://leetcode-cn.com/problems/long-pressed-name/description/
#
# algorithms
# Easy (40.11%)
# Likes:    96
# Dislikes: 0
# Total Accepted:    14.7K
# Total Submissions: 36.7K
# Testcase Example:  '"alex"\n"aaleex"'
#
# 你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
#
# 你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
#
#
#
# 示例 1：
#
# 输入：name = "alex", typed = "aaleex"
# 输出：true
# 解释：'alex' 中的 'a' 和 'e' 被长按。
#
#
# 示例 2：
#
# 输入：name = "saeed", typed = "ssaaedd"
# 输出：false
# 解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
#
#
# 示例 3：
#
# 输入：name = "leelee", typed = "lleeelee"
# 输出：true
#
#
# 示例 4：
#
# 输入：name = "laiden", typed = "laiden"
# 输出：true
# 解释：长按名字中的字符并不是必要的。
#
#
#
#
# 提示：
#
#
# name.length <= 1000
# typed.length <= 1000
# name 和 typed 的字符都是小写字母。
#
#
#
#
#
#
#


# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j, m, n = 0, 0, len(name), len(typed)
        while j < n:
            if i < m and typed[j] == name[i]:
                i += 1
                j += 1
            elif 0 < j and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == m


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.isLongPressedName("alex", "aaleex"))
    print(solu.isLongPressedName("saeed", "ssaaedd"))
    print(solu.isLongPressedName("leelee", "lleeelee"))
    print(solu.isLongPressedName("laiden", "laiden"))
    print(solu.isLongPressedName("kikcxmvzi", "kiikcxxmmvvzz"))
    print(solu.isLongPressedName("alex", "alexxr"))

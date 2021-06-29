#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   168.excel表列名称.py
@Time    :   2021/06/29 09:03:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (40.14%)
# Likes:    369
# Dislikes: 0
# Total Accepted:    55.8K
# Total Submissions: 139.1K
# Testcase Example:  '1'
#
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
#
# 例如，
#
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB
# ⁠   ...
#
#
# 示例 1:
#
# 输入: 1
# 输出: "A"
#
#
# 示例 2:
#
# 输入: 28
# 输出: "AB"
#
#
# 示例 3:
#
# 输入: 701
# 输出: "ZY"
#
#
#


# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []

        while columnNumber:
            columnNumber -= 1
            ans.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26

        ans.reverse()
        return ''.join(ans)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.convertToTitle(1))
    print(solu.convertToTitle(25))
    print(solu.convertToTitle(26))
    print(solu.convertToTitle(27))
    print(solu.convertToTitle(701))
    print(solu.convertToTitle(702))
    print(solu.convertToTitle(703))

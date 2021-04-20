#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   171.excel表列序号.py
@Time    :   2021/04/20 22:23:37
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#
# https://leetcode-cn.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (69.03%)
# Likes:    217
# Dislikes: 0
# Total Accepted:    67.6K
# Total Submissions: 97.9K
# Testcase Example:  '"A"'
#
# 给定一个Excel表格中的列名称，返回其相应的列序号。
#
# 例如，
#
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28
# ⁠   ...
#
#
# 示例 1:
#
# 输入: "A"
# 输出: 1
#
#
# 示例 2:
#
# 输入: "AB"
# 输出: 28
#
#
# 示例 3:
#
# 输入: "ZY"
# 输出: 701
#
# 致谢：
# 特别感谢 @ts 添加此问题并创建所有测试用例。
#
#


# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for ch in columnTitle:
            ans = ans * 26 + ord(ch) - ord('A') + 1
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.titleToNumber(""))
    print(solu.titleToNumber("A"))
    print(solu.titleToNumber("B"))
    print(solu.titleToNumber("Z"))
    print(solu.titleToNumber("AA"))  # 27
    print(solu.titleToNumber("AB"))
    print(solu.titleToNumber("AZ"))  # 52
    print(solu.titleToNumber("BA"))  # 53
    print(solu.titleToNumber("ZY"))
    print(solu.titleToNumber("ZZ"))  # 702
    print(solu.titleToNumber("AAA"))  # 703

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   118.杨辉三角.py
@Time    :   2020/08/07 22:36:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (66.99%)
# Likes:    336
# Dislikes: 0
# Total Accepted:    96.1K
# Total Submissions: 143.4K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
#
#
from typing import List


# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []

        ans, i = [[1]], 1
        while i < numRows:
            row = [1]
            for j in range(1, i):
                row.append(ans[i - 1][j - 1] + ans[i - 1][j])
            row.append(1)

            ans.append(row)
            i += 1

        return ans


# @lc code=end

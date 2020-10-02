#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   119.杨辉三角-ii.py
@Time    :   2020/10/02 21:59:09
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (61.91%)
# Likes:    183
# Dislikes: 0
# Total Accepted:    71.8K
# Total Submissions: 115.9K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]
#
#
# 进阶：
#
# 你可以优化你的算法到 O(k) 空间复杂度吗？
#
#
from typing import List


# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = [1]
        for i in range(1, rowIndex + 1):
            cur = [1]
            for j in range(1, i):
                cur.append(pre[j - 1] + pre[j])
            cur.append(1)
            pre = cur
        return pre


# @lc code=end

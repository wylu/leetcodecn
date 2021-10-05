#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1037.有效的回旋镖.py
@Time    :   2021/10/05 13:28:50
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] 有效的回旋镖
#
# https://leetcode-cn.com/problems/valid-boomerang/description/
#
# algorithms
# Easy (43.85%)
# Likes:    29
# Dislikes: 0
# Total Accepted:    9.6K
# Total Submissions: 21.8K
# Testcase Example:  '[[1,1],[2,3],[3,2]]'
#
# 回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。
#
# 给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。
#
#
#
# 示例 1：
#
# 输入：[[1,1],[2,3],[3,2]]
# 输出：true
#
#
# 示例 2：
#
# 输入：[[1,1],[2,2],[3,3]]
# 输出：false
#
#
#
# 提示：
#
#
# points.length == 3
# points[i].length == 2
# 0 <= points[i][j] <= 100
#
#
#
from typing import List


# @lc code=start
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p1, p2, p3 = points
        return ((p2[1] - p1[1]) * (p3[0] - p1[0]) !=
                (p3[1] - p1[1]) * (p2[0] - p1[0]))


# @lc code=end

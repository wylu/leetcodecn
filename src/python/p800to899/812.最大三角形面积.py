#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   812.最大三角形面积.py
@Time    :   2022/05/15 09:36:10
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#
# https://leetcode-cn.com/problems/largest-triangle-area/description/
#
# algorithms
# Easy (63.19%)
# Likes:    100
# Dislikes: 0
# Total Accepted:    12.7K
# Total Submissions: 20.2K
# Testcase Example:  '[[0,0],[0,1],[1,0],[0,2],[2,0]]'
#
# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
#
#
# 示例:
# 输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# 输出: 2
# 解释:
# 这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
#
#
#
#
# 注意:
#
#
# 3 <= points.length <= 50.
# 不存在重复的点。
# -50 <= points[i][j] <= 50.
# 结果误差值在 10^-6 以内都认为是正确答案。
#
#
#
from typing import List


# @lc code=start
class Solution:

    def largestTriangleArea(self, points: List[List[int]]) -> float:

        def area(p1: List[int], p2: List[int], p3: List[int]) -> float:
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return 0.5 * abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 -
                             x3 * y2)

        ans, n = 0, len(points)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    ans = max(ans, area(points[i], points[j], points[k]))

        return ans


# @lc code=end

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   780.到达终点.py
@Time    :   2022/04/09 18:18:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=780 lang=python3
#
# [780] 到达终点
#
# https://leetcode-cn.com/problems/reaching-points/description/
#
# algorithms
# Hard (36.08%)
# Likes:    202
# Dislikes: 0
# Total Accepted:    16.4K
# Total Submissions: 45.3K
# Testcase Example:  '1\n1\n3\n5'
#
# 给定四个整数 sx , sy ，tx 和 ty，如果通过一系列的转换可以从起点 (sx, sy) 到达终点 (tx, ty)，则返回 true，否则返回
# false。
#
# 从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)。
#
#
#
# 示例 1:
#
#
# 输入: sx = 1, sy = 1, tx = 3, ty = 5
# 输出: true
# 解释:
# 可以通过以下一系列转换从起点转换到终点：
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
#
#
# 示例 2:
#
#
# 输入: sx = 1, sy = 1, tx = 2, ty = 2
# 输出: false
#
#
# 示例 3:
#
#
# 输入: sx = 1, sy = 1, tx = 1, ty = 1
# 输出: true
#
#
#
#
# 提示:
#
#
# 1 <= sx, sy, tx, ty <= 10^9
#
#
#


# @lc code=start
class Solution:

    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty and tx != ty:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx

        if tx == sx and ty == sy:
            return True

        if tx == sx:
            return ty > sy and (ty - sy) % tx == 0

        if ty == sy:
            return tx > sx and (tx - sx) % ty == 0

        return False


# @lc code=end

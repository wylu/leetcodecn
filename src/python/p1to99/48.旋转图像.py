#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   48.旋转图像.py
@Time    :   2020/07/29 00:00:46
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
# https://leetcode-cn.com/problems/rotate-image/description/
#
# algorithms
# Medium (68.86%)
# Likes:    506
# Dislikes: 0
# Total Accepted:    86.5K
# Total Submissions: 125.5K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个 n × n 的二维矩阵表示一个图像。
#
# 将图像顺时针旋转 90 度。
#
# 说明：
#
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
#
# 示例 1:
#
# 给定 matrix =
# [
# ⁠ [1,2,3],
# ⁠ [4,5,6],
# ⁠ [7,8,9]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
# ⁠ [7,4,1],
# ⁠ [8,5,2],
# ⁠ [9,6,3]
# ]
#
#
# 示例 2:
#
# 给定 matrix =
# [
# ⁠ [ 5, 1, 9,11],
# ⁠ [ 2, 4, 8,10],
# ⁠ [13, 3, 6, 7],
# ⁠ [15,14,12,16]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
# ⁠ [15,13, 2, 5],
# ⁠ [14, 3, 4, 1],
# ⁠ [12, 6, 8, 9],
# ⁠ [16, 7,10,11]
# ]
#
#
#

from typing import List
"""
转置 + 反转

1, 2, 3        1, 4, 7        7, 4, 1
4, 5, 6   ->   2, 5, 8   ->   8, 5, 2
7, 8, 9        3, 6, 9        9, 6, 3
"""


# @lc code=start
class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        n = len(mat)
        # 转置 list(map(list,zip(*matrix)))
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            # 反转
            mat[i].reverse()


# @lc code=end

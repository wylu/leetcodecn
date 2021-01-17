#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1232.缀点成线.py
@Time    :   2021/01/17 21:13:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#
# https://leetcode-cn.com/problems/check-if-it-is-a-straight-line/description/
#
# algorithms
# Easy (46.84%)
# Likes:    69
# Dislikes: 0
# Total Accepted:    25.4K
# Total Submissions: 54.2K
# Testcase Example:  '[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]'
#
# 在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y]
# 表示横坐标为 x、纵坐标为 y 的点。
#
# 请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。
#
#
#
# 示例 1：
#
#
#
# 输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# 输出：true
#
#
# 示例 2：
#
#
#
# 输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# 输出：false
#
#
#
#
# 提示：
#
#
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates 中不含重复的点
#
#
#
from typing import List
"""
方法一：数学
思路

记数组 coordinates 中的点为 P[0],P[1],...,P[n-1]。为方便后续计算，
将所有点向 (-P[0][0], -P[0][1]) 方向平移。记平移后的点为 P[0]', P[1]',
..., P[n-1]'，其中 P[i]' = (P[i][0] - P[0][0], P[i][1] - P[0][1]),
位于坐标系原点 O 上。

由于经过两点的直线有且仅有一条，我们以 P[0]'和 P[1]'，来确定这条直线。

因为 P[0]' 位于坐标系原点 O 上，直线过原点，故设其方程为 Ax + By = 0，
将 P[1]' 坐标代入可得 A = P[1][1]', B = -P[1][0]'。

然后依次判断 P[2]', P[3]', ..., P[n-1]' 是否在这条直线上，将其坐标代入
直线方程即可。
"""


# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        dx, dy = coordinates[0]
        A, B = coordinates[1][1] - dy, -(coordinates[1][0] - dx)
        for i in range(2, len(coordinates)):
            x, y = coordinates[i][0] - dx, coordinates[i][1] - dy
            if A * x + B * y != 0:
                return False
        return True


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    print(solu.checkStraightLine(coordinates))

    coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
    print(solu.checkStraightLine(coordinates))

    coordinates = [[1, 1], [1, 2], [1, 3]]
    print(solu.checkStraightLine(coordinates))

    coordinates = [[1, 1], [2, 1], [3, 1]]
    print(solu.checkStraightLine(coordinates))

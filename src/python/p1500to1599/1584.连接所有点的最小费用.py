#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1584.连接所有点的最小费用.py
@Time    :   2021/01/19 22:36:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#
# https://leetcode-cn.com/problems/min-cost-to-connect-all-points/description/
#
# algorithms
# Medium (65.82%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    16.8K
# Total Submissions: 25.5K
# Testcase Example:  '[[0,0],[2,2],[3,10],[5,2],[7,0]]'
#
# 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
#
# 连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示
# val 的绝对值。
#
# 请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。
#
#
#
# 示例 1：
#
#
#
#
# 输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# 输出：20
# 解释：
#
# 我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
# 注意到任意两个点之间只有唯一一条路径互相到达。
#
#
# 示例 2：
#
#
# 输入：points = [[3,12],[-2,5],[-4,1]]
# 输出：18
#
#
# 示例 3：
#
#
# 输入：points = [[0,0],[1,1],[1,0],[-1,1]]
# 输出：4
#
#
# 示例 4：
#
#
# 输入：points = [[-1000000,-1000000],[1000000,1000000]]
# 输出：4000000
#
#
# 示例 5：
#
#
# 输入：points = [[0,0]]
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= points.length <= 1000
# -10^6 <= xi, yi <= 10^6
# 所有点 (xi, yi) 两两不同。
#
#
#
from typing import List
"""
最小生成树
"""


# @lc code=start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = (abs(points[i][0] - points[j][0]) +
                              abs(points[i][1] - points[j][1]))
                cost[j][i] = cost[i][j]

        ans = 0
        used = [False] * n  # 顶点i是否在集合X中
        mincost = [0x7FFFFFFF] * n  # 从集合X出发的边到每个顶点的最小权值
        mincost[0] = 0

        while True:
            v = -1
            # 从不属于X的顶点中选取从X到其权值最小的顶点
            for u in range(n):
                if not used[u] and (v == -1 or mincost[u] < mincost[v]):
                    v = u

            if v == -1:
                break

            used[v] = True  # 把顶点v加入X
            ans += mincost[v]  # 把边的权值加到结果里

            # 更新集合X到其它顶点的最小权值
            for u in range(n):
                mincost[u] = min(mincost[u], cost[v][u])

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(solu.minCostConnectPoints(points))

    points = [[3, 12], [-2, 5], [-4, 1]]
    print(solu.minCostConnectPoints(points))

    points = [[0, 0], [1, 1], [1, 0], [-1, 1]]
    print(solu.minCostConnectPoints(points))

    points = [[-1000000, -1000000], [1000000, 1000000]]
    print(solu.minCostConnectPoints(points))

    points = [[0, 0]]
    print(solu.minCostConnectPoints(points))

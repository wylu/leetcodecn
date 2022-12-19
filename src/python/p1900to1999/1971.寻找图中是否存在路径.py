#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1971.寻找图中是否存在路径.py
@Time    :   2022/12/19 09:32:16
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=1971 lang=python3
#
# [1971] 寻找图中是否存在路径
#
# https://leetcode.cn/problems/find-if-path-exists-in-graph/description/
#
# algorithms
# Easy (45.46%)
# Likes:    66
# Dislikes: 0
# Total Accepted:    10.2K
# Total Submissions: 20.8K
# Testcase Example:  '3\n[[0,1],[1,2],[2,0]]\n0\n2'
#
# 有一个具有 n 个顶点的 双向 图，其中每个顶点标记从 0 到 n - 1（包含 0 和 n - 1）。图中的边用一个二维整数数组 edges 表示，其中
# edges[i] = [ui, vi] 表示顶点 ui 和顶点 vi 之间的双向边。 每个顶点对由 最多一条 边连接，并且没有顶点存在与自身相连的边。
#
# 请你确定是否存在从顶点 source 开始，到顶点 destination 结束的 有效路径 。
#
# 给你数组 edges 和整数 n、source 和 destination，如果从 source 到 destination 存在 有效路径 ，则返回
# true，否则返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# 输出：true
# 解释：存在由顶点 0 到顶点 2 的路径:
# - 0 → 1 → 2
# - 0 → 2
#
#
# 示例 2：
#
#
# 输入：n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination =
# 5
# 输出：false
# 解释：不存在由顶点 0 到顶点 5 的路径.
#
#
#
#
# 提示：
#
#
# 1 <= n <= 2 * 10^5
# 0 <= edges.length <= 2 * 10^5
# edges[i].length == 2
# 0 <= ui, vi <= n - 1
# ui != vi
# 0 <= source, destination <= n - 1
# 不存在重复边
# 不存在指向顶点自身的边
#
#
#
from typing import List


# @lc code=start
class UnionFind:

    def __init__(self, n: int) -> None:
        self.par = list(range(n))

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> None:
        self.par[self.find(x)] = self.par[self.find(y)]


class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int,
                  destination: int) -> bool:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.find(source) == uf.find(destination)


# @lc code=end

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1489.找到最小生成树里的关键边和伪关键边.py
@Time    :   2021/01/21 23:42:03
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1489 lang=python3
#
# [1489] 找到最小生成树里的关键边和伪关键边
#
# https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/
#
# algorithms
# Hard (70.45%)
# Likes:    88
# Dislikes: 0
# Total Accepted:    9.4K
# Total Submissions: 13.3K
# Testcase Example:
# '5\n[[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]'
#
# 给你一个 n 个点的带权无向连通图，节点编号为 0 到 n-1 ，同时还有一个数组 edges ，其中 edges[i] = [fromi, toi,
# weighti] 表示在 fromi 和 toi 节点之间有一条带权无向边。最小生成树 (MST)
# 是给定图中边的一个子集，它连接了所有节点且没有环，而且这些边的权值和最小。
#
#
# 请你找到给定图中最小生成树的所有关键边和伪关键边。如果从图中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。伪关键边则是可能会出现在某些最小生成树中但不会出现在所有最小生成树中的边。
#
# 请注意，你可以分别以任意顺序返回关键边的下标和伪关键边的下标。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# 输出：[[0,1],[2,3,4,5]]
# 解释：上图描述了给定图。
# 下图是所有的最小生成树。
#
# 注意到第 0 条边和第 1 条边出现在了所有最小生成树中，所以它们是关键边，我们将这两个下标作为输出的第一个列表。
# 边 2，3，4 和 5 是所有 MST 的剩余边，所以它们是伪关键边。我们将它们作为输出的第二个列表。
#
#
# 示例 2 ：
#
#
#
# 输入：n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# 输出：[[],[0,1,2,3]]
# 解释：可以观察到 4 条边都有相同的权值，任选它们中的 3 条可以形成一棵 MST 。所以 4 条边都是伪关键边。
#
#
#
#
# 提示：
#
#
# 2 <= n <= 100
# 1 <= edges.length <= min(200, n * (n - 1) / 2)
# edges[i].length == 3
# 0 <= fromi < toi < n
# 1 <= weighti <= 1000
# 所有 (fromi, toi) 数对都是互不相同的。
#
#
#
from typing import List
"""
方法一：枚举 + 最小生成树判定
思路与算法

我们首先需要理解题目描述中对于「关键边」和「伪关键边」的定义：

关键边：如果最小生成树中删去某条边，会导致最小生成树的权值和增加，那么
我们就说它是一条关键边。也就是说，如果设原图最小生成树的权值为 value，
那么去掉这条边后：
  - 要么整个图不连通，不存在最小生成树；
  - 要么整个图联通，对应的最小生成树的权值为 v，其严格大于 value。

伪关键边：可能会出现在某些最小生成树中但不会出现在所有最小生成树中的边。
也就是说，我们可以在计算最小生成树的过程中，最先考虑这条边，即最先将
这条边的两个端点在并查集中合并。设最终得到的最小生成树权值为 v，如果
v = value，那么这条边就是伪关键边。

需要注意的是，关键边也满足伪关键边对应的性质。因此，我们首先对原图执行
Kruskal 算法，得到最小生成树的权值 value，随后我们枚举每一条边，首先
根据上面的方法判断其是否是关键边，如果不是关键边，再判断其是否是伪关键边。
"""


# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.size = [1] * n
        self.n = n
        self.cnt = n  # 当前连通分量的数目

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        self.par[fx] = self.par[fy]
        self.size[fx] += self.size[fy]
        self.cnt -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]
                                           ) -> List[List[int]]:
        m = len(edges)
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])

        # 计算 value
        uf = UnionFind(n)
        value = 0
        for edge in edges:
            if uf.union(edge[0], edge[1]):
                value += edge[2]

        ans = [[], []]

        for i in range(m):
            # 判断是否为关键边
            uf = UnionFind(n)
            v = 0
            for j in range(m):
                if i != j and uf.union(edges[j][0], edges[j][1]):
                    v += edges[j][2]

            if uf.cnt != 1 or (uf.cnt == 1 and v > value):
                ans[0].append(edges[i][3])
                continue

            # 判断是否为伪关键边
            uf = UnionFind(n)
            uf.union(edges[i][0], edges[i][1])
            v = edges[i][2]
            for j in range(m):
                if i != j and uf.union(edges[j][0], edges[j][1]):
                    v += edges[j][2]

            if v == value:
                ans[1].append(edges[i][3])

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    n = 5
    edges = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3],
             [1, 4, 6]]
    print(solu.findCriticalAndPseudoCriticalEdges(n, edges))

    n = 4
    edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]
    print(solu.findCriticalAndPseudoCriticalEdges(n, edges))

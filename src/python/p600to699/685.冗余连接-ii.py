#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   685.冗余连接-ii.py
@Time    :   2020/09/17 21:40:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=685 lang=python3
#
# [685] 冗余连接 II
#
# https://leetcode-cn.com/problems/redundant-connection-ii/description/
#
# algorithms
# Hard (43.15%)
# Likes:    164
# Dislikes: 0
# Total Accepted:    11.9K
# Total Submissions: 27.5K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。
#
# 输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N)
# 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
#
# 结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u 和顶点 v 的边，其中 u 是 v 的一个父节点。
#
# 返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。
#
# 示例 1:
#
# 输入: [[1,2], [1,3], [2,3]]
# 输出: [2,3]
# 解释: 给定的有向图如下:
# ⁠ 1
# ⁠/ \
# v   v
# 2-->3
#
#
# 示例 2:
#
# 输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# 输出: [4,1]
# 解释: 给定的有向图如下:
# 5 <- 1 -> 2
# ⁠    ^    |
# ⁠    |    v
# ⁠    4 <- 3
#
#
# 注意:
#
#
# 二维数组大小的在3到1000范围内。
# 二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。
#
#
#
from typing import List
"""
方法一：并查集
思路与算法

在一棵树中，边的数量比节点的数量少 1。如果一棵树有 N 个节点，则这棵树有
N-1 条边。这道题中的图在树的基础上多了一条附加的边，因此边的数量也是 N。

树中的每个节点都有一个父节点，除了根节点没有父节点。在多了一条附加的边之后，
可能有以下两种情况：
  1.附加的边指向根节点，则包括根节点在内的每个节点都有一个父节点，此时图中
    一定有环路；
  2.附加的边指向非根节点，则恰好有一个节点（即被附加的边指向的节点）有两个
    父节点，此时图中可能有环路也可能没有环路。

要找到附加的边，需要遍历图中的所有的边构建出一棵树，在构建树的过程中寻找
导致冲突（即导致一个节点有两个父节点）的边以及导致环路出现的边。

具体做法是，使用数组 parent 记录每个节点的父节点，初始时对于任何 1 <= i <= N
都有 parent[i] = i，另外创建并查集，初始时并查集中的每个节点都是一个连通分支，
该连通分支的根节点就是该节点本身。遍历每条边的过程中，维护导致冲突的边和导致
环路出现的边，由于只有一条附加的边，因此最多有一条导致冲突的边和一条导致环路
出现的边。

当访问到边 [u,v] 时，进行如下操作：
  1.如果此时已经有 parent[v] = v，说明 v 有两个父节点，将当前的边 [u,v]
    记为导致冲突的边；
  2.否则，令 parent[v] = u，然后在并查集中分别找到 u 和 v 的祖先（即各自
    的连通分支中的根节点），如果祖先相同，说明这条边导致环路出现，将当前的边
    [u,v] 记为导致环路出现的边，如果祖先不同，则在并查集中将 u 和 v 进行合并。

根据上述操作，同一条边不可能同时被记为导致冲突的边和导致环路出现的边。如果
访问到的边确实同时导致冲突和环路出现，则这条边被记为导致冲突的边。

在遍历图中的所有边之后，根据是否存在导致冲突的边和导致环路出现的边，得到
附加的边。

如果没有导致冲突的边，说明附加的边一定导致环路出现，而且是在环路中的最后
一条被访问到的边，因此附加的边即为导致环路出现的边。

如果有导致冲突的边，记这条边为 [u,v]，则有两条边指向 v，另一条边为
[parent[v],v]，需要通过判断是否有导致环路的边决定哪条边是附加的边。
  1.如果有导致环路的边，则附加的边不可能是 [u,v]（因为 [u,v] 已经被记为
    导致冲突的边，不可能被记为导致环路出现的边），因此附加的边是
    [parent[v],v]。
  2.如果没有导致环路的边，则附加的边是后被访问到的指向 v 的边，因此附加
    的边是 [u,v]。

有冲突，有环：
    例如：[[2,1],[3,1],[1,4],[4,2]]
    此时导致冲突的边为 [3,1]，导致环路的边为 [4,2]，所以附加的边是：[2,1]

有冲突，无环：
    例如：[[3,1],[2,1],[1,4],[4,2]]
    此时导致冲突的边为 [2,1]，没有导致环路的边（因为我们记录的导致冲突
    的边不会用来建图），所以附加的边是：[2,1]
"""


# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))

    def union(self, x: int, y: int) -> None:
        self.par[self.find(x)] = self.find(y)

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]


class Solution:
    def findRedundantDirectedConnection(self,
                                        edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n + 1)
        parent = list(range(n + 1))
        conflict, cycle = -1, -1
        for i, (u, v) in enumerate(edges):
            if parent[v] != v:
                conflict = i
            else:
                parent[v] = u
                if uf.find(u) == uf.find(v):
                    cycle = i
                else:
                    uf.union(u, v)

        if conflict == -1:
            return edges[cycle]

        if cycle == -1:
            return edges[conflict]
        v = edges[conflict][1]
        return [parent[v], v]


# @lc code=end

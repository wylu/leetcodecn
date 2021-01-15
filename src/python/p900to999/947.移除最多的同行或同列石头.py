#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   947.移除最多的同行或同列石头.py
@Time    :   2021/01/15 21:52:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=947 lang=python3
#
# [947] 移除最多的同行或同列石头
#
# https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/description/
#
# algorithms
# Medium (59.47%)
# Likes:    175
# Dislikes: 0
# Total Accepted:    17K
# Total Submissions: 28.6K
# Testcase Example:  '[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]'
#
# n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。
#
# 如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。
#
# 给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子
# 的最大数量。
#
#
#
# 示例 1：
#
#
# 输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# 输出：5
# 解释：一种移除 5 块石头的方法如下所示：
# 1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
# 2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
# 3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
# 4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
# 5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
# 石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。
#
# 示例 2：
#
#
# 输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# 输出：3
# 解释：一种移除 3 块石头的方法如下所示：
# 1. 移除石头 [2,2] ，因为它和 [2,0] 同行。
# 2. 移除石头 [2,0] ，因为它和 [0,0] 同列。
# 3. 移除石头 [0,2] ，因为它和 [0,0] 同行。
# 石头 [0,0] 和 [1,1] 不能移除，因为它们没有与另一块石头同行/列。
#
# 示例 3：
#
#
# 输入：stones = [[0,0]]
# 输出：0
# 解释：[0,0] 是平面上唯一一块石头，所以不可以移除它。
#
#
#
# 提示：
#
#
# 1 <= stones.length <= 1000
# 0 <= xi, yi <= 10^4
# 不会有两块石头放在同一个坐标点上
#
#
#
# from collections import defaultdict
from typing import List
"""
方法一：深度优先搜索
思路及解法

我们将这个二维平面抽象成图，把石子看作「点」，石子间的同行或同列关系看作
「边」。如果两个石子同属某一行或某一列，我们就认为这两个石子之间有一条边。
由题意可知，对于任意一个点，只要有点和它相连，我们就可以将其删除。

显然，对于任意一个连通图，我们总可以通过调整节点的删除顺序，把这个连通图
中删到只剩下一个节点。本题中我们不需要关注如何安排删除顺序，只需要了解
这个性质即可。

拓展：对于希望进一步拓展的同学，这里给出一个方法：从连通块中处理出任意
一个生成树，该生成树的以任意一点为根节点的后序遍历均为可行解。

这样我们只需要统计整张图中有多少个极大连通子图（也叫做连通块或连通分量）
即可。最终能够留下来的点的数量，即为连通块的数量。我们用总点数减去连通块
的数量，即可知道我们可以删去的点的最大数量。

在实际代码实现中，我们首先枚举计算任意两点间的连通性，然后使用深度优先
搜索的方式计算连通块的数量即可。

方法二：优化建图 + 深度优先搜索
思路及解法

注意到方法一中，建图的效率太过低下，我们考虑对其优化。

注意到任意两点间之间直接相连与间接相连并无影响，即我们只关注两点间的
连通性，而不关注具体如何联通。因此考虑对于拥有 kk 个石子的任意一行或
一列，我们都恰使用 k-1 条边进行连接。这样我们就可以将边数从 O(n^2)
的数量级降低到 O(n)。

这样，我们首先利用哈希表存储每一行或每一列所拥有的石子，然后分别处理
每一行或每一列的连通属性即可。

注意到每一个石子的横坐标与纵坐标的范围均在 [1,10^4]，因此在实际代码中，
我们可以使用同一张哈希表，只需要令纵坐标加 10^4，以区别横坐标与纵坐标
即可。

方法三：优化建图 + 并查集
思路及解法

我们也可以变换思路，在方法一与方法二中，我们维护的是石子，实际上我们
也可以直接维护石子所在的行与列。

实际操作时，我们直接将每一个石子的行与列进行合并即可，可以理解为，
每一个点不是与其他所有点进行连接，而是连接到自己所在的行与列上，
由行与列进行合并。

同时，既然我们只关注连通性本身，我们就可以利用并查集维护连通性。
在实际代码中，我们以哈希表为底层数据结构实现父亲数组 f，最后哈希表
中所有的键均为出现过的行与列，我们计算有多少行与列的父亲恰为自己，
即可知道连通块的数量。
"""


# @lc code=start
class UnionFind:
    def __init__(self):
        self.par = {}
        self.cnt = 0

    def find(self, x: int) -> int:
        if x not in self.par:
            self.par[x] = x
            self.cnt += 1

        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> None:
        fx, fy = self.find(x), self.find(y)
        if fx != fy:
            self.par[fx] = self.par[fy]
            self.cnt -= 1


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()
        for x, y in stones:
            uf.union(x, y + 10001)
        return len(stones) - uf.cnt


# @lc code=end

# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         n = len(stones)
#         rc = defaultdict(list)
#         graph = []
#         for i in range(n):
#             graph.append([])
#             rc[stones[i][0]].append(i)
#             rc[stones[i][1] + 10001].append(i)

#         for _, vec in rc.items():
#             for i in range(1, len(vec)):
#                 graph[vec[i - 1]].append(vec[i])
#                 graph[vec[i]].append(vec[i - 1])

#         def dfs(u: int) -> None:
#             visit[u] = True
#             for v in graph[u]:
#                 if not visit[v]:
#                     dfs(v)

#         visit = [False] * n
#         cnt = 0
#         for i in range(n):
#             if not visit[i]:
#                 dfs(i)
#                 cnt += 1

#         return n - cnt

# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         n = len(stones)
#         graph = []
#         for i in range(n):
#             graph.append([])
#             for j in range(n):
#                 if (stones[i][0] == stones[j][0]
#                         or stones[i][1] == stones[j][1]):
#                     graph[i].append(j)

#         def dfs(u: int) -> None:
#             visit[u] = True
#             for v in graph[u]:
#                 if not visit[v]:
#                     dfs(v)

#         visit = [False] * n
#         cnt = 0
#         for i in range(n):
#             if not visit[i]:
#                 dfs(i)
#                 cnt += 1

#         return n - cnt

if __name__ == "__main__":
    solu = Solution()
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    print(solu.removeStones(stones))

    stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
    print(solu.removeStones(stones))

    stones = [[0, 0]]
    print(solu.removeStones(stones))

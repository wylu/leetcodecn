#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1203.项目管理.py
@Time    :   2021/01/12 22:24:09
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1203 lang=python3
#
# [1203] 项目管理
#
# https://leetcode-cn.com/problems/sort-items-by-groups-respecting-dependencies/description/
#
# algorithms
# Hard (64.34%)
# Likes:    137
# Dislikes: 0
# Total Accepted:    8.6K
# Total Submissions: 13.4K
# Testcase Example:
# '8\n2\n[-1,-1,1,0,0,1,0,-1]\n[[],[6],[5],[6],[3,6],[],[],[]]'
#
# 公司共有 n 个项目和  m 个小组，每个项目要不无人接手，要不就由 m 个小组之一负责。
#
# group[i] 表示第 i 个项目所属的小组，如果这个项目目前无人接手，那么 group[i] 就等于
# -1。（项目和小组都是从零开始编号的）小组可能存在没有接手任何项目的情况。
#
# 请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表：
#
#
# 同一小组的项目，排序后在列表中彼此相邻。
# 项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i
# 个项目左侧）应该完成的所有项目。
#
#
# 如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个 空列表 。
#
#
#
# 示例 1：
#
#
#
#
# 输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
# [[],[6],[5],[6],[3,6],[],[],[]]
# 输出：[6,3,4,1,5,2,0,7]
#
#
# 示例 2：
#
#
# 输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
# [[],[6],[5],[6],[3],[],[4],[]]
# 输出：[]
# 解释：与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。
#
#
#
#
# 提示：
#
#
# 1 <= m <= n <= 3 * 10^4
# group.length == beforeItems.length == n
# -1 <= group[i] <= m - 1
# 0 <= beforeItems[i].length <= n - 1
# 0 <= beforeItems[i][j] <= n - 1
# i != beforeItems[i][j]
# beforeItems[i] 不含重复元素
#
#
#
from collections import defaultdict
from collections import deque
from typing import List
"""
方法一：拓扑排序
思路与算法

做出这道题首先需要了解「拓扑排序」的相关知识。

拓扑排序简单来说，是对于一张有向图 G，我们需要将 G 的 n 个点排列成一组序列，
使得图中任意一对顶点 <u,v>，如果图中存在一条 u→v 的边，那么 u 在序列中需要
出现在 v 的前面。整个算法的具体过程这里不再展开赘述。如果对相关的知识还不是
很熟悉，可以参考「207. 课程表的官方题解」。

回到题目中，我们可以将项目抽象成点，项目间依赖关系的抽象成边，即如果进行
项目 i 前需要完成项目 j，那么就存在一条 j→i 的边。然后判断图中是否可以
拓扑排序。

但这样的方法忽略了题目中的一个关键条件：「同一小组的项目，排序后在列表中
彼此相邻」。这意味着组与组之间也存在依赖关系，故还要解决组之间的拓扑排序。
基于此，解决这道题其实可以分成两步：

首先解决组与组的依赖关系。我们将组抽象成点，组与组的关系抽象成边，建图后
判断是否存在一个拓扑排序。

如果存在拓扑顺序 groupTopSort，我们只要再确定组内的依赖关系。遍历组间的
拓扑序 groupTopSort，对于任意的组 g，对所有属于组 g 的点再进行拓扑排序。
如果能够拓扑排序，则将组 g 内部的拓扑序按顺序放入答案数组即可。

实现细节

注意到某些项目存在无人接手的情况，由于这些 groupId 都为 -1，为了编码方便，
我们重新将其编号。由于已有的小组编号不会超过 m-1，因此可以将这些项目从 m
开始正序编号，这样能保证不会与已存在的小组编号冲突。

为了减少编码的复杂度，我们可以将拓扑排序抽成一个函数进行复用，定义
topSort(deg, graph, items) 表示当前待拓扑排序的点集为 items，点的入度
数组为 deg，点的连边关系为 graph，graph[i] 表示点 i 连出点组成的集合，
如果不存在冲突，返回拓扑排序后的数组，否则返回一个空数组。

在建图的过程中，如果发现两个项目属于不同的项目组，则在组间的关系图中添加
对应的边，否则在组内的关系图中添加对应的边。
"""


# @lc code=start
class Solution:
    def sortItems(self, n: int, m: int, group: List[int],
                  beforeItems: List[List[int]]) -> List[int]:
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = m
                m += 1

        groupGraph = [[] for _ in range(m)]
        itemGraph = [[] for _ in range(n)]
        groupDeg = [0] * m
        itemDeg = [0] * n

        for i in range(len(group)):
            for j in beforeItems[i]:
                if group[j] != group[i]:
                    groupGraph[group[j]].append(group[i])
                    groupDeg[group[i]] += 1

        for i in range(n):
            for j in beforeItems[i]:
                itemGraph[j].append(i)
                itemDeg[i] += 1

        groupSortRes = self.topologicalSort(groupGraph, groupDeg, m)
        if not groupSortRes:
            return []

        itemSortRes = self.topologicalSort(itemGraph, itemDeg, n)
        if not itemSortRes:
            return []

        groups2items = defaultdict(list)
        for item in itemSortRes:
            groups2items[group[item]].append(item)

        ans = []
        for groupId in groupSortRes:
            ans += groups2items[groupId]

        return ans

    def topologicalSort(self, graph: List[List[int]], deg: List[int],
                        n: int) -> List[int]:
        res = []
        que = deque([i for i in range(n) if deg[i] == 0])

        while que:
            u = que.popleft()
            res.append(u)
            for v in graph[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    que.append(v)

        return res if len(res) == n else []


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    n = 5
    m = 5
    group = [2, 0, -1, 3, 0]
    beforeItems = [[2, 1, 3], [2, 4], [], [], []]
    print(solu.sortItems(n, m, group, beforeItems))

    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
    print(solu.sortItems(n, m, group, beforeItems))

    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[], [6], [5], [6], [3], [], [4], []]
    print(solu.sortItems(n, m, group, beforeItems))

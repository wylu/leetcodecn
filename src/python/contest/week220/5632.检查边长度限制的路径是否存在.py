#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5632.检查边长度限制的路径是否存在.py
@Time    :   2020/12/20 11:28:01
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
方法一：并查集 + 离线处理

我们将 queries 按照 limit[j] 从小到大进行排序，这样所有的询问中对边权
的限制就单调递增了。

同时，我们将 edgeList 按照 dis[i] 从小到大进行排序，这样所有的边权
也就单调递增了。

此时我们就可以愉快地处理所有的询问了。我们使用并查集维护图的连通性，
并且使用指针 i 表示当前往并查集中添加的最后一条边。当我们处理到询问
queries[j] = (p[j], q[j], limit[j]) 时，由于 limit[j] 是单调递增的，
因此我们只需要往并查集中添加新的边，即不断地在 edgeList 中向右移动指针
i，直到当前指向的边权 dis[i] >= limit[j] 为止。随后我们只需要使用
并查集判断 p[j] 和 q[j] 是否连通即可。

将 queries 和 edgeList 进行排序的巧妙之处就在于，我们实际上做了这样
的一个操作：
  - 我们将所有的 queries 和 edgeList 合并在一起，并且按照边权或者边权
    限制进行排序。在出现相等的情况时，queries 或者 edgeList 内部的
    相对顺序并不重要，但所有的 queries 必须要排在所有的 edgeList 之前，
    这是因为题目中要求对于每一个询问，可以经过的边权是严格小于边权限制的；
  - 在排序之后，我们依次遍历所有的元素。如果当前元素是 queries，我们就
    使用并查集进行查询（询问两个点是否连通）操作；如果当前元素是
    edgeList，我们就是用并查集进行修改（添加一条边）操作。
"""
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> None:
        self.par[self.find(x)] = self.find(y)

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]],
                                  queries: List[List[int]]) -> List[bool]:
        # 将 queries 按照边权限制从小到大排序
        indices = list(range(len(queries)))
        indices.sort(key=lambda x: queries[x][2])
        # 将 edgeList 按照边权从小到大排序
        edgeList.sort(key=lambda x: x[2])

        ans = [False] * len(queries)
        uf = UnionFind(n)
        j, m = 0, len(edgeList)
        for i in indices:
            u, v, val = queries[i]
            while j < m and edgeList[j][2] < val:
                uf.union(edgeList[j][0], edgeList[j][1])
                j += 1
            ans[i] = uf.connected(u, v)

        return ans


if __name__ == "__main__":
    solu = Solution()
    n = 3
    edgeList = [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]]
    queries = [[0, 1, 2], [0, 2, 5]]
    print(solu.distanceLimitedPathsExist(n, edgeList, queries))

    n = 5
    edgeList = [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]]
    queries = [[0, 4, 14], [1, 4, 13]]
    print(solu.distanceLimitedPathsExist(n, edgeList, queries))

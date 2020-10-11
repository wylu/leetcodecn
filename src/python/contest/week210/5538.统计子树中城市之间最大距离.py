#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5538.统计子树中城市之间最大距离.py
@Time    :   2020/10/11 10:48:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def countSubgraphsForEachDiameter(self, n: int,
                                      edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def comb(cur: int, cnt: int, tar: int, stack: List[int]) -> None:
            if cnt == tar:
                trees.append(stack[::])
                return
            for i in range(cur, n + 1):
                stack.append(i)
                comb(i + 1, cnt + 1, tar, stack)
                stack.pop()

        def dfs(u: int, ress: set, parent: -1) -> int:
            if not graph[u] or not ress:
                return 0
            dists = []
            for v in graph[u]:
                if v in ress:
                    ress.remove(v)
                    dists.append(dfs(v, ress, u))
            dists.sort()
            if len(dists) == 0:
                return 0
            elif len(dists) == 1:
                return 1 + dists[0]
            else:
                if parent == -1:
                    return 2 + sum(dists[-2:])
                else:
                    return 1 + max(dists[-2:])

        ans = [0] * (n - 1)
        trees, stack = [], []
        for i in range(2, n + 1):
            comb(1, 0, i, stack)

        print(trees)

        for t in trees:
            root, ress = t[0], set(t[1:])
            d = dfs(root, ress, -1)
            if not ress:
                ans[d - 1] += 1

        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.countSubgraphsForEachDiameter(4, [[1, 2], [2, 3], [2, 4]]))

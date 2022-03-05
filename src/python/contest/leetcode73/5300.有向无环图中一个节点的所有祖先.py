#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5300.有向无环图中一个节点的所有祖先.py
@Time    :   2022/03/05 22:45:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from collections import deque
from typing import List


class Solution:

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]

        ins, graph = [0] * n, defaultdict(list)
        for u, v in edges:
            ins[v] += 1
            graph[u].append(v)

        que = deque(i for i, c in enumerate(ins) if c == 0)
        while que:
            u = que.popleft()
            for v in graph[u]:
                ans[v].update(ans[u])
                ans[v].add(u)
                ins[v] -= 1

                if ins[v] == 0:
                    que.append(v)

        return [sorted(item) for item in ans]


if __name__ == '__main__':
    solu = Solution()
    n = 8
    edgeList = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7],
                [4, 6]]
    print(solu.getAncestors(n, edgeList))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6135.图中的最长环.py
@Time    :   2022/07/31 11:22:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import Counter
from typing import List


class Solution:

    def longestCycle(self, edges: List[int]) -> int:
        graph = {u: v for u, v in enumerate(edges) if v != -1}
        # print(graph)
        while True:
            flag = True
            loop = set(graph.values())
            for k in list(graph.keys()):
                if k not in loop:
                    del graph[k]
                    flag = False

            if flag:
                break

        ins = Counter(graph.values())
        # print(ins)
        seen = set()

        def dfs(node: int) -> int:
            dist = 0
            while node not in seen and node in graph:
                seen.add(node)
                node = graph[node]
                dist += 1
            return dist if node in seen else -1

        ans = -1
        for k, v in ins.items():
            if v == 1 and k not in seen:
                ans = max(ans, dfs(k))

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.longestCycle(edges=[3, 3, 4, 2, 3]))
    print(solu.longestCycle(edges=[2, -1, 3, 1]))
    print(solu.longestCycle(edges=[2, 6, 4, 7, 6, 0, 8, -1, 4]))

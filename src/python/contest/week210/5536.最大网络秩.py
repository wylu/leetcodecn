#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5536.最大网络秩.py
@Time    :   2020/10/11 10:34:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        ans = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                cnt = len(graph[i]) + len(graph[j])
                if j in graph[i]:
                    cnt -= 1
                ans = max(ans, cnt)

        return ans

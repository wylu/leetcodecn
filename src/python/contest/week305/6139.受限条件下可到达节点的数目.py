#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6139.受限条件下可到达节点的数目.py
@Time    :   2022/08/07 10:33:34
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

    def reachableNodes(self, n: int, edges: List[List[int]],
                       restricted: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = {0}
        restricted = set(restricted)
        que = deque([0])
        while que:
            for _ in range(len(que)):
                u = que.popleft()
                for v in graph[u]:
                    if v not in seen and v not in restricted:
                        seen.add(v)
                        que.append(v)

        return len(seen)

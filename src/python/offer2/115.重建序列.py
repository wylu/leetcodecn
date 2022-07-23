#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   115.重建序列.py
@Time    :   2022/07/23 10:18:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import deque
from typing import List


class Solution:

    def sequenceReconstruction(self, nums: List[int],
                               sequences: List[List[int]]) -> bool:
        n = len(nums)
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for seq in sequences:
            for i in range(1, len(seq)):
                x, y = seq[i - 1] - 1, seq[i] - 1
                graph[x].append(y)
                indeg[y] += 1

        que = deque([i for i, d in enumerate(indeg) if d == 0])
        while que:
            if len(que) > 1:
                return False

            x = que.popleft()
            for y in graph[x]:
                indeg[y] -= 1
                if indeg[y] == 0:
                    que.append(y)

        return True

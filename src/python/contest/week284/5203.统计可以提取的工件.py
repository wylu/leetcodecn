#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5203.统计可以提取的工件.py
@Time    :   2022/03/13 10:44:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def digArtifacts(self, n: int, artifacts: List[List[int]],
                     dig: List[List[int]]) -> int:
        graph = [[1] * n for _ in range(n)]
        for r, c in dig:
            graph[r][c] = 0

        ans = 0
        for r1, c1, r2, c2 in artifacts:
            cur = 0
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    cur += graph[i][j]

            if cur == 0:
                ans += 1

        return ans

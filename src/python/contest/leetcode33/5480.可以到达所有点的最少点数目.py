#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5480.可以到达所有点的最少点数目.py
@Time    :   2020/08/22 22:37:47
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int,
                                  edges: List[List[int]]) -> List[int]:
        inds = [0] * n
        for u, v in edges:
            inds[v] += 1

        ans = []
        for i, val in enumerate(inds):
            if val == 0:
                ans.append(i)
        return ans

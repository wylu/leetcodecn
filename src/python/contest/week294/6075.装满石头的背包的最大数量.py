#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6075.装满石头的背包的最大数量.py
@Time    :   2022/05/22 10:32:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def maximumBags(self, capacity: List[int], rocks: List[int],
                    additionalRocks: int) -> int:
        ans = 0
        gaps = sorted(c - r for c, r in zip(capacity, rocks))
        gaps.reverse()
        while additionalRocks and gaps and additionalRocks >= gaps[-1]:
            ans += 1
            additionalRocks -= gaps[-1]
            gaps.pop()
        return ans

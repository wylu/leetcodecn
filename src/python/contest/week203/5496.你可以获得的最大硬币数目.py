#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5496.你可以获得的最大硬币数目.py
@Time    :   2020/08/23 11:04:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        ans = 0
        i, j = 0, len(piles) - 1
        while i + 1 < j:
            ans += piles[j - 1]
            j -= 2
            i += 1

        return ans

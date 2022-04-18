#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1.宝石补给.py
@Time    :   2022/04/16 15:00:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for x, y in operations:
            half = gem[x] // 2
            gem[x] -= half
            gem[y] += half

        return max(gem) - min(gem)

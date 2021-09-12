#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5868.可互换矩形的组数.py
@Time    :   2021/09/12 10:37:18
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        counter = defaultdict(int)
        for w, h in rectangles:
            counter[w / h] += 1

        ans = 0
        for _, cnt in counter.items():
            ans += cnt * (cnt - 1) // 2

        return ans

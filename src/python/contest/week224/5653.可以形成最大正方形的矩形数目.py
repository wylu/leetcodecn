#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5653.可以形成最大正方形的矩形数目.py
@Time    :   2021/01/17 10:30:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen, cnt = 0, 0
        for h, w in rectangles:
            cur = min(h, w)
            if cur == maxLen:
                cnt += 1
            elif cur > maxLen:
                maxLen = cur
                cnt = 1
        return cnt

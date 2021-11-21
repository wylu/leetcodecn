#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5930.两栋颜色不同且距离最远的房子.py
@Time    :   2021/11/21 10:30:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        n = len(colors)
        for i in range(n - 1):
            for j in range(n - 1, i, -1):
                if colors[j] != colors[i]:
                    ans = max(ans, j - i)
                    break
        return ans

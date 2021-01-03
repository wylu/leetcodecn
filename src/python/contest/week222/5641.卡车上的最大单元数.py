#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5641.卡车上的最大单元数.py
@Time    :   2021/01/03 10:30:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        ans, i, n = 0, 0, len(boxTypes)
        while i < n and truckSize > 0:
            cnt = min(boxTypes[i][0], truckSize)
            ans += cnt * boxTypes[i][1]
            i += 1
            truckSize -= cnt

        return ans

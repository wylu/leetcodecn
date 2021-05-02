#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5746.到目标元素的最小距离.py
@Time    :   2021/05/02 10:30:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = 0x80000000
        for i, num in enumerate(nums):
            if num == target:
                ans = min(ans, abs(i - start))
        return ans

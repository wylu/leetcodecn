#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5767.检查是否区域内所有整数都被覆盖.py
@Time    :   2021/06/12 22:30:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int,
                  right: int) -> bool:
        seen = set()
        for area in ranges:
            for num in range(area[0], area[1] + 1):
                seen.add(num)

        for num in range(left, right + 1):
            if num not in seen:
                return False

        return True

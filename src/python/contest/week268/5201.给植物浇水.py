#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5201.给植物浇水.py
@Time    :   2021/11/21 10:37:50
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        cur = capacity
        for i, plant in enumerate(plants):
            if cur < plant:
                ans += i + i + 1
                cur = capacity - plant
            else:
                ans += 1
                cur -= plant
        return ans

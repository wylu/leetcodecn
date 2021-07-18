#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5814.新增的最少台阶数.py
@Time    :   2021/07/18 10:33:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        ans = pre = 0
        for cur in rungs:
            if cur - pre <= dist:
                pre = cur
                continue
            ans += (cur - pre - 1) // dist
            pre = cur
        return ans

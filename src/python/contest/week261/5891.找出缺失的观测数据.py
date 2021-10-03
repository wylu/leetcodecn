#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5891.找出缺失的观测数据.py
@Time    :   2021/10/03 10:35:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        tot = mean * (m + n)

        rolls_tot = sum(rolls)
        need_tot = tot - rolls_tot

        if need_tot < n or need_tot > n * 6:
            return []

        ans = []
        for i in range(n, 0, -1):
            d, r = divmod(need_tot, i)
            if r:
                d += 1
            ans.append(d)
            need_tot -= d
        return ans

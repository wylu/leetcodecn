#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5954.给植物浇水II.py
@Time    :   2021/12/12 11:20:11
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int,
                      capacityB: int) -> int:
        ans = 0
        n = len(plants)
        i, j = 0, n - 1
        alice, bob = capacityA, capacityB

        while i < j:
            if alice < plants[i]:
                ans += 1
                alice = capacityA
            if bob < plants[j]:
                ans += 1
                bob = capacityB

            alice -= plants[i]
            i += 1
            bob -= plants[j]
            j -= 1

        if i == j:
            if max(alice, bob) < plants[i]:
                ans += 1

        return ans

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5512.统计不开心的朋友.py
@Time    :   2020/09/13 10:41:03
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]],
                       pairs: List[List[int]]) -> int:
        firend = {}
        for x, y in pairs:
            firend[x] = y
            firend[y] = x

        ans = 0
        for x in range(n):
            z = 0
            while z < len(preferences[x]) and preferences[x][z] != firend[x]:
                z += 1

            if z == 0:
                continue

            for y in preferences[x][:z]:
                p = 0
                while p < len(preferences[y]) and preferences[y][p] != x:
                    p += 1
                q = 0
                while q < len(
                        preferences[y]) and preferences[y][q] != firend[y]:
                    q += 1
                if p < q:
                    ans += 1
                    break

        return ans

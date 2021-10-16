#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5886.如果相邻两个颜色均相同则删除当前颜色.py
@Time    :   2021/10/16 22:34:58
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        colors += '#'
        alice = bob = 0
        i, j, n = 0, 0, len(colors)
        while i < n - 1:
            if colors[i] != colors[i + 1]:
                if colors[i] == 'A':
                    alice += max(0, (i - j - 1))
                else:
                    bob += max(0, i - j - 1)
                j = i + 1
            i += 1

        return alice > bob

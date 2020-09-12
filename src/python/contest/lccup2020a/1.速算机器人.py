#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1.速算机器人.py
@Time    :   2020/09/12 15:00:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def calculate(self, s: str) -> int:
        x, y = 1, 0
        for ch in s:
            if ch == 'A':
                x = 2 * x + y
            else:
                y = 2 * y + x
        return x + y

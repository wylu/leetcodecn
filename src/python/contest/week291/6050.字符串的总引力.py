#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6050.字符串的总引力.py
@Time    :   2022/05/01 10:56:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def appealSum(self, s: str) -> int:
        ans, tot, pos = 0, 0, [-1] * 26
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            tot += i - pos[c]
            ans += tot
            pos[c] = i
        return ans

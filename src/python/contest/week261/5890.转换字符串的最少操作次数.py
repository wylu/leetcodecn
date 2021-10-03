#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5890.转换字符串的最少操作次数.py
@Time    :   2021/10/03 10:30:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def minimumMoves(self, s: str) -> int:
        ans, n, i = 0, len(s), 0
        while i < n:
            if s[i] == 'O':
                i += 1
                continue

            ans += 1
            i += 3

        return ans

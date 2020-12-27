#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5637.判断字符串的两半是否相似.py
@Time    :   2020/12/27 10:30:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vols = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        n = len(s)
        a, b = s[:n // 2], s[n // 2:]

        def count(s: str) -> int:
            cnt = 0
            for ch in s:
                if ch in vols:
                    cnt += 1
            return cnt

        return count(a) == count(b)

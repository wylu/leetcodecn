#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   实现strStr().py
@Time    :   2020/07/30 12:43:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def strStr(self, s: str, p: str) -> int:
        if not p:
            return 0
        if not s:
            return -1

        next = self.calNext(p)
        i, j = 0, 0
        while i < len(s) and j < len(p):
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = next[j]

        return i - j if j == len(p) else -1

    def calNext(self, p: str) -> List[int]:
        n = len(p)
        next = [-1] * n
        k, j = -1, 0

        while j < n - 1:
            if k == -1 or p[k] == p[j]:
                k += 1
                j += 1
                next[j] = k
            else:
                k = next[k]

        return next

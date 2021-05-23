#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5763.哪种连续子字符串更长.py
@Time    :   2021/05/23 10:30:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        c0 = c1 = 0

        if s[0] == '0':
            c0 = 1
        else:
            c1 = 1

        n = len(s)
        pre, cur = 0, 1
        while cur < n:
            while cur < n and s[cur] == s[pre]:
                cur += 1
            if s[pre] == '0':
                c0 = max(c0, cur - pre)
            else:
                c1 = max(c1, cur - pre)
            pre = cur
        return c1 > c0

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5483.整理字符串.py
@Time    :   2020/08/09 10:30:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return ''

        while True:
            o = []
            i, n, flag = 0, len(s), True
            while i < n:
                if i < n - 1 and abs(ord(s[i]) - ord(s[i + 1])) == 32:
                    i += 2
                    flag = False
                else:
                    o.append(s[i])
                    i += 1
            s = ''.join(o)

            if flag:
                break

        return s

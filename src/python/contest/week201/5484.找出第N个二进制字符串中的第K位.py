#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5484.找出第N个二进制字符串中的第K位.py
@Time    :   2020/08/09 10:46:59
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.s(n)[k - 1]

    def s(self, i: int) -> str:
        if i == 1:
            return '0'
        r = self.s(i - 1)
        return r + '1' + self.reverse(r)

    def reverse(self, x: str) -> str:
        r = []
        for c in x:
            r.append('1' if c == '0' else '0')
        r.reverse()
        return ''.join(r)

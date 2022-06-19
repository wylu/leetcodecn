#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5242.兼具大小写的最好英文字母.py
@Time    :   2022/06/19 10:30:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def greatestLetter(self, s: str) -> str:
        ans = ''
        ss = set(s)
        for i in range(26):
            ch1 = chr(ord('a') + i)
            ch2 = chr(ord('A') + i)
            if ch1 in ss and ch2 in ss:
                ans = ch2
        return ans

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   罗马数字转整数.py
@Time    :   2020/08/05 22:04:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0

        roma = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0
        i = len(s) - 1
        while i >= 0:
            ans += roma[s[i]]

            if i > 0:
                if (s[i] == 'V' or s[i] == 'X') and s[i - 1] == 'I':
                    ans -= 1
                    i -= 1
                elif (s[i] == 'L' or s[i] == 'C') and s[i - 1] == 'X':
                    ans -= 10
                    i -= 1
                elif (s[i] == 'D' or s[i] == 'M') and s[i - 1] == 'C':
                    ans -= 100
                    i -= 1

            i -= 1

        return ans

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5543.两个相同字符之间的最长子字符串.py
@Time    :   2020/10/18 10:30:56
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        ans = -1
        for i in range(n - 1):
            for j in range(n - 1, i, -1):
                if s[i] == s[j]:
                    ans = max(ans, j - i - 1)
        return ans

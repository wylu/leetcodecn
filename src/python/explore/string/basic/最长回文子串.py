#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   最长回文子串.py
@Time    :   2020/10/02 14:37:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        n = len(s)
        start, end = 0, 0

        def expandAroundCenter(left: int, right: int) -> tuple:
            while 0 <= left and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            l1, r1 = expandAroundCenter(i, i)
            l2, r2 = expandAroundCenter(i, i + 1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]

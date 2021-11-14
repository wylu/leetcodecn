#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5910.检查两个字符串是否几乎相等.py
@Time    :   2021/11/13 22:30:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = [0] * 26, [0] * 26
        for ch in word1:
            cnt1[ord(ch) - ord('a')] += 1
        for ch in word2:
            cnt2[ord(ch) - ord('a')] += 1

        for i in range(26):
            if abs(cnt1[i] - cnt2[i]) > 3:
                return False

        return True

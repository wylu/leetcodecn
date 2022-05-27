#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   17.11.单词距离.py
@Time    :   2022/05/27 14:50:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        ans = 0x7FFFFFFF
        p1, p2 = -1, -1
        for i, word in enumerate(words):
            if word == word1:
                p1 = i
            elif word == word2:
                p2 = i

            if p1 != -1 and p2 != -1:
                ans = min(ans, abs(p1 - p2))

        return ans

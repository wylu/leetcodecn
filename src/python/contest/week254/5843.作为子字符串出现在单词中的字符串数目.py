#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5843.作为子字符串出现在单词中的字符串数目.py
@Time    :   2021/08/15 10:30:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for p in patterns:
            if p in word:
                ans += 1
        return ans

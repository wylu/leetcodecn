#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5784.重新分配字符使所有字符串都相等.py
@Time    :   2021/06/13 10:30:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt = defaultdict(int)
        for word in words:
            for ch in word:
                cnt[ch] += 1

        n = len(words)
        for val in cnt.values():
            if val % n != 0:
                return False

        return True

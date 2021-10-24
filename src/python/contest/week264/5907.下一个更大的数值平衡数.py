#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5907.下一个更大的数值平衡数.py
@Time    :   2021/10/24 10:50:56
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def check(n: int) -> bool:
            cnt = defaultdict(int)
            for ch in str(n):
                cnt[ch] += 1

            for key, value in cnt.items():
                if int(key) != value:
                    return False

            return True

        while True:
            n += 1
            if check(n):
                return n

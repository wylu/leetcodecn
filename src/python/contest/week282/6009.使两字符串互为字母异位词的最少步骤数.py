#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6009.使两字符串互为字母异位词的最少步骤数.py
@Time    :   2022/02/27 10:31:47
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import Counter


class Solution:

    def minSteps(self, s: str, t: str) -> int:
        cs, ct = Counter(s), Counter(t)

        ans = 0
        for i in range(26):
            ch = chr(ord('a') + i)
            ans += abs(cs[ch] - ct[ch])

        return ans

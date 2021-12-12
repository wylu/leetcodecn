#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5952.环和杆.py
@Time    :   2021/12/12 10:30:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict


class Solution:
    def countPoints(self, rings: str) -> int:
        cnt = [defaultdict(int) for _ in range(10)]
        for i in range(0, len(rings), 2):
            cnt[int(rings[i + 1])][rings[i]] += 1

        ans = 0
        for item in cnt:
            if item['R'] and item['G'] and item['B']:
                ans += 1

        return ans

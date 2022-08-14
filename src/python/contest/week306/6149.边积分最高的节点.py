#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6149.边积分最高的节点.py
@Time    :   2022/08/14 10:37:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:

    def edgeScore(self, edges: List[int]) -> int:
        cnt = defaultdict(list)
        for u, v in enumerate(edges):
            cnt[v].append(u)

        ans = score = 0
        for v, us in cnt.items():
            total = sum(us)
            if total > score:
                ans, score = v, total
            elif total == score:
                ans = min(ans, v)

        return ans

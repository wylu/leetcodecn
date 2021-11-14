#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5926.买票需要的时间.py
@Time    :   2021/11/14 10:30:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans, n = 0, len(tickets)

        while True:
            for i in range(n):
                if tickets[i] == 0:
                    continue
                tickets[i] -= 1
                ans += 1
                if tickets[k] == 0:
                    return ans

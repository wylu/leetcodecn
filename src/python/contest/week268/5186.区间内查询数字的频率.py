#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5186.区间内查询数字的频率.py
@Time    :   2021/11/21 10:44:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import bisect
from collections import defaultdict
from typing import List


class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.pos = defaultdict(list)
        for i, num in enumerate(arr):
            self.pos[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.pos:
            return 0

        positions = self.pos[value]
        lti = bisect.bisect_left(positions, left)
        rti = bisect.bisect_right(positions, right)
        return rti - lti


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

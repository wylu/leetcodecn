#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5527.大小为 K 的不重叠线段的数目.py
@Time    :   2020/10/17 23:06:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import math


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return math.comb(n + k - 1, 2 * k) % 1000000007

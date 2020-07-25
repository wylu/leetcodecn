#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5459.形成目标数组的子数组最少增加次数.py
@Time    :   2020/07/26 01:26:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        for i in range(1, len(target)):
            ans += max(target[i] - target[i - 1], 0)
        return ans

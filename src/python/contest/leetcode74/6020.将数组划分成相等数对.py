#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6020.将数组划分成相等数对.py
@Time    :   2022/03/19 22:32:33
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import Counter
from typing import List


class Solution:

    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for _, cnt in counter.items():
            if cnt % 2 != 0:
                return False
        return True

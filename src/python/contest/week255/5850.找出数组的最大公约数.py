#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5850.找出数组的最大公约数.py
@Time    :   2021/08/22 10:30:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import math
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maximum, minimum = 0, 1010
        for num in nums:
            maximum = max(maximum, num)
            minimum = min(minimum, num)

        return math.gcd(maximum, minimum)

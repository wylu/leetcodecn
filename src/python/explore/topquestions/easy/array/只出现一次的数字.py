#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   只出现一次的数字.py
@Time    :   2020/07/26 10:03:11
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :   n ^ n = 0, n ^ 0 = n
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for e in nums:
            ans ^= e
        return ans

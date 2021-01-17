#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5243.同积元组.py
@Time    :   2021/01/17 10:34:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                cnt[nums[i] * nums[j]] += 1

        ans = 0
        for _, v in cnt.items():
            ans += (v * (v - 1) // 2) * 8

        return ans

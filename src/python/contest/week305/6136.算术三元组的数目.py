#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6136.算术三元组的数目.py
@Time    :   2022/08/07 10:30:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        ans += 1
        return ans

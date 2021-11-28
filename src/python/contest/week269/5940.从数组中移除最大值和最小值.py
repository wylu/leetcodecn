#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5940.从数组中移除最大值和最小值.py
@Time    :   2021/11/28 10:49:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_idx = max_idx = 0
        for i, num in enumerate(nums):
            if num < nums[min_idx]:
                min_idx = i
            if num > nums[max_idx]:
                max_idx = i

        if min_idx > max_idx:
            min_idx, max_idx = max_idx, min_idx

        res1 = max_idx + 1
        res2 = len(nums) - min_idx
        res3 = min_idx + 1 + len(nums) - max_idx

        return min(res1, res2, res3)

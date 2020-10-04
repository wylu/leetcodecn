#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5531.特殊数组的特征值.py
@Time    :   2020/10/04 10:30:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n, j = len(nums), 0
        for i in range(1, nums[-1] + 1):
            while j < n and nums[j] < i:
                j += 1
            if n - j == i:
                return i
        return -1

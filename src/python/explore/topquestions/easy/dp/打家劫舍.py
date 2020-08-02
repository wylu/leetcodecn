#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   打家劫舍.py
@Time    :   2020/08/02 16:45:09
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        f0, f1 = 0, nums[0]
        for i in range(len(nums) - 1):
            f0, f1 = max(f0, f1), f0 + nums[i + 1]

        return max(f0, f1)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5755.数组中最大数对和的最小值.py
@Time    :   2021/05/29 22:37:17
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        nums.sort()
        for i in range(n // 2 + 1):
            ans = max(ans, nums[i] + nums[n - i - 1])
        return ans

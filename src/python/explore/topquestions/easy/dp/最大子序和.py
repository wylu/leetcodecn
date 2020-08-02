#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   最大子序和.py
@Time    :   2020/08/02 16:18:49
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, cur = nums[0], nums[0]

        for i in range(1, len(nums)):
            if cur > 0:
                cur += nums[i]
            else:
                cur = nums[i]

            ans = max(ans, cur)

        return ans

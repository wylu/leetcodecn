#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5854.学生分数的最小差值.py
@Time    :   2021/08/29 10:30:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]

        for i in range(k - 1, len(nums)):
            j = i - k + 1
            ans = min(ans, nums[i] - nums[j])

        return ans

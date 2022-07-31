#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6132.使数组中所有元素都等于零.py
@Time    :   2022/07/31 10:30:18
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def minimumOperations(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        while True:
            if not any(nums):
                return ans

            x = min(num for num in nums if num > 0)
            for i in range(n):
                if nums[i] > 0:
                    nums[i] -= x

            ans += 1

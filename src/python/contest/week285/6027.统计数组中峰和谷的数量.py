#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6027.统计数组中峰和谷的数量.py
@Time    :   2022/03/20 10:30:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def countHillValley(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            if arr and num == arr[-1]:
                continue
            arr.append(num)

        ans = 0
        for i in range(1, len(arr) - 1):
            if (arr[i - 1] < arr[i] > arr[i + 1]
                    or arr[i - 1] > arr[i] < arr[i + 1]):
                ans += 1

        return ans

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   两数之和II-输入有序数组.py
@Time    :   2020/10/02 16:38:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            cur = nums[i] + nums[j]
            if cur == target:
                return i + 1, j + 1
            if cur < target:
                i += 1
            else:
                j -= 1
        return [-1, -1]

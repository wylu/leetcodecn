#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   两数之和.py
@Time    :   2020/07/26 10:22:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []

        map = {}
        for i in range(len(nums)):
            if target - nums[i] in map:
                return [map[target - nums[i]], i]
            map[nums[i]] = i

        return []

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5938.找出数组排序后的目标下标.py
@Time    :   2021/11/28 10:30:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            if num == target:
                ans.append(i)
        return ans

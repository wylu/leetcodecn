#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5894.至少在两个数组中出现的值.py
@Time    :   2021/10/10 10:30:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int],
                      nums3: List[int]) -> List[int]:
        counter = defaultdict(int)
        for nums in [set(nums1), set(nums2), set(nums3)]:
            for num in nums:
                counter[num] += 1
        return [k for k, v in counter.items() if v > 1]

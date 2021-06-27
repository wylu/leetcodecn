#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5797.两个数对之间的最大乘积差.py
@Time    :   2021/06/27 10:30:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]

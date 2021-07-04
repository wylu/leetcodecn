#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5800.基于排列构建数组.py
@Time    :   2021/07/04 10:30:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]

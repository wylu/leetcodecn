#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5855.找出数组中的第K大整数.py
@Time    :   2021/08/29 10:34:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted(map(int, nums), reverse=True)
        return str(nums[k - 1])

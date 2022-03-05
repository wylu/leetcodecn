#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6024.数组中紧跟key之后出现最频繁的数字.py
@Time    :   2022/03/05 22:30:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:

    def mostFrequent(self, nums: List[int], key: int) -> int:
        cnts = defaultdict(int)
        for i in range(len(nums) - 1):
            if nums[i] == key:
                cnts[nums[i + 1]] += 1

        ans, cnt = 0, 0
        for n, c in cnts.items():
            if c > cnt:
                ans, cnt = n, c

        return ans

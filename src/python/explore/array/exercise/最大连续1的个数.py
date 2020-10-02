#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   最大连续1的个数.py
@Time    :   2020/10/02 16:52:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, cnt = 0, 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
        return max(ans, cnt)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5468.第 k 个缺失的正整数.py
@Time    :   2020/08/08 22:30:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = set(arr)
        i, cnt = 0, 0
        while cnt < k:
            i += 1
            if i not in nums:
                cnt += 1
        return i


# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         nums = [0] * 2001
#         for i in arr:
#             nums[i] = i

#         i, cnt = 0, 0
#         while cnt < k:
#             i += 1
#             if nums[i] == 0:
#                 cnt += 1
#         return i

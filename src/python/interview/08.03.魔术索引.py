#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   08.03.魔术索引.py
@Time    :   2020/07/31 09:21:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        i = 0
        while i < len(nums):
            if nums[i] == i:
                return i

            if i < nums[i]:
                i = nums[i]
            else:
                i += 1

        return -1


# class Solution:
#     def findMagicIndex(self, nums: List[int]) -> int:
#         if not nums:
#             return -1

#         for i in range(len(nums)):
#             if nums[i] == i:
#                 return i

#         return -1

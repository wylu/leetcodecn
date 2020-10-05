#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   两个数组的交集.py
@Time    :   2020/10/05 11:02:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums1 = set(nums1)
        return list(set(num for num in nums2 if num in nums1))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   两个数组的交集II.py
@Time    :   2020/10/05 11:11:47
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        cnts = defaultdict(int)
        for num in nums1:
            cnts[num] += 1
        ans = []
        for num in nums2:
            if cnts[num] > 0:
                ans.append(num)
                cnts[num] -= 1
        return ans

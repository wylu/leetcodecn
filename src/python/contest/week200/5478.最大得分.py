#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5478.最大得分.py
@Time    :   2020/08/02 11:37:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = 0, 0
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                sum1 += nums1[i]
                i += 1
                sum2 += nums2[j]
                j += 1
                sum1 = sum2 = max(sum1, sum2)

        while i < n1:
            sum1 += nums1[i]
            i += 1

        while j < n2:
            sum2 += nums2[j]
            j += 1

        return max(sum1, sum2) % (10**9 + 7)

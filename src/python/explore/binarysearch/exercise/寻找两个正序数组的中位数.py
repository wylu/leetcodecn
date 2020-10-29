#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   寻找两个正序数组的中位数.py
@Time    :   2020/10/05 12:24:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        totLeft = (m + n + 1) // 2

        left, right = 0, m
        while left < right:
            i = (left + right + 1) // 2
            j = totLeft - i
            if nums1[i - 1] <= nums2[j]:
                left = i
            else:
                right = i - 1

        i = (left + right + 1) // 2
        j = totLeft - i
        INT_MIN, INT_MAX = -0x80000000, 0x7FFFFFFF
        maxLeft1 = INT_MIN if i == 0 else nums1[i - 1]
        minRight1 = INT_MAX if i == m else nums1[i]
        maxLeft2 = INT_MIN if j == 0 else nums2[j - 1]
        minRight2 = INT_MAX if j == n else nums2[j]

        if (m + n) % 2 == 0:
            return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
        return max(maxLeft1, maxLeft2)

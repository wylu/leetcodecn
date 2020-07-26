#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   两个数组的交集II.py
@Time    :   2020/07/26 10:06:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        cnt = {}
        for e in nums1:
            cnt[e] = cnt.get(e, 0) + 1

        ans = []
        for e in nums2:
            if e in cnt and cnt[e] > 0:
                ans.append(e)
                cnt[e] -= 1

        return ans

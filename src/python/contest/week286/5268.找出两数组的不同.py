#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5268.找出两数组的不同.py
@Time    :   2022/03/27 10:30:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def findDifference(self, nums1: List[int],
                       nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]

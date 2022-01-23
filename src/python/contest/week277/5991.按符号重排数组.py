#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5991.按符号重排数组.py
@Time    :   2022/01/23 10:37:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        i, j, n = 0, 0, len(nums)
        while len(ans) < n:
            while nums[i] < 0:
                i += 1
            ans.append(nums[i])
            i += 1

            while nums[j] > 0:
                j += 1
            ans.append(nums[j])
            j += 1

        return ans

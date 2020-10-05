#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   找出第k小的距离对.py
@Time    :   2020/10/06 00:25:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        def ok(dist: int) -> bool:
            cnt = i = 0
            for j in range(n):
                while nums[j] - nums[i] > dist:
                    i += 1
                cnt += j - i
            return cnt < k

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if ok(mid):
                left = mid + 1
            else:
                right = mid

        return left

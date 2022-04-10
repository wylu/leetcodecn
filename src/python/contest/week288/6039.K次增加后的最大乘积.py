#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6039.K次增加后的最大乘积.py
@Time    :   2022/04/10 10:52:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import heapq
from typing import List


class Solution:

    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k:
            num = heapq.heappop(nums)
            num += 1
            k -= 1
            heapq.heappush(nums, num)

        ans, MOD = 1, 10**9 + 7
        for num in nums:
            ans = (ans * num) % MOD

        return ans

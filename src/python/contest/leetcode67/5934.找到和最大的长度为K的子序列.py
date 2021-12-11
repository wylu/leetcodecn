#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5934.找到和最大的长度为K的子序列.py
@Time    :   2021/12/11 22:30:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = sorted(nums)
        cnt = defaultdict(int)
        for num in arr[-k:]:
            cnt[num] += 1

        ans = []
        for num in nums:
            if cnt[num] > 0:
                ans.append(num)
                cnt[num] -= 1

        return ans

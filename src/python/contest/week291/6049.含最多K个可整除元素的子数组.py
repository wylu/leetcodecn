#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6049.含最多K个可整除元素的子数组.py
@Time    :   2022/05/01 10:41:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        ans, n = 0, len(nums)

        seen = set()
        for i in range(n):
            for j in range(i, n):
                stk, cnt = [], 0
                for num in nums[i:j + 1]:
                    if num % p == 0:
                        cnt += 1
                    stk.append(num)

                if cnt > k:
                    break

                seq = tuple(stk)
                if seq not in seen:
                    ans += 1
                    seen.add(seq)

        return ans

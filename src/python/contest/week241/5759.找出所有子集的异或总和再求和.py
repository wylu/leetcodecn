#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5759.找出所有子集的异或总和再求和.py
@Time    :   2021/05/16 10:30:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)

        def dfs(xor: int, cur: int) -> None:
            nonlocal ans
            if cur == n:
                ans += xor
                return

            dfs(xor ^ nums[cur], cur + 1)
            dfs(xor, cur + 1)

        dfs(0, 0)
        return ans

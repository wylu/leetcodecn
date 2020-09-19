#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   目标和.py
@Time    :   2020/09/19 17:32:56
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from functools import lru_cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(c: int, target: int) -> int:
            if c == n:
                return int(target == S)
            return dfs(c + 1, target + nums[c]) + dfs(c + 1, target - nums[c])

        return dfs(0, 0)


if __name__ == '__main__':
    solu = Solution()
    print(solu.findTargetSumWays([1, 1, 1], 2))
    print(solu.findTargetSumWays([1, 1, 1, 1, 1], 3))
    print(
        solu.findTargetSumWays([
            40, 2, 49, 50, 46, 6, 5, 23, 38, 45, 45, 17, 4, 26, 40, 33, 14, 9,
            37, 24
        ], 7))

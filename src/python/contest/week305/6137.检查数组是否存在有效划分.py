#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6137.检查数组是否存在有效划分.py
@Time    :   2022/08/07 10:39:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from functools import lru_cache
from typing import List


class Solution:

    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)
        def dfs(start: int) -> bool:
            if start == n:
                return True
            if start + 1 >= n:
                return False

            i, j, k = start, start + 1, start + 2
            if nums[i] == nums[j]:
                if dfs(k) or (k < n and nums[i] == nums[k] and dfs(k + 1)):
                    return True
            else:
                if (k < n and nums[i] + 1 == nums[j] and nums[i] + 2 == nums[k]
                        and dfs(k + 1)):
                    return True

            return False

        return dfs(0)


if __name__ == '__main__':
    solu = Solution()
    print(solu.validPartition(nums=[4, 4, 4, 5, 6]))
    print(solu.validPartition(nums=[1, 1, 1, 2]))

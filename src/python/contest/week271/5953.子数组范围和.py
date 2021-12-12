#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5953.子数组范围和.py
@Time    :   2021/12/12 10:34:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n - 1):
            mininum, maximum = 0x7FFFFFFF, -0x80000000
            for j in range(i, n):
                mininum = min(mininum, nums[j])
                maximum = max(maximum, nums[j])
                ans += maximum - mininum

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.subArrayRanges(nums=[1, 2, 3]))
    print(solu.subArrayRanges(nums=[4, -2, -3, 4, 1]))

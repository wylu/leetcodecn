#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6017.向数组中追加K个整数.py
@Time    :   2022/03/06 10:37:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import bisect
from typing import List


class Solution:

    def minimalKSum(self, nums: List[int], k: int) -> int:
        total = ((1 + k) * k) // 2
        nums.sort()
        idx = bisect.bisect_right(nums, k)

        total -= sum(set(nums[:idx]))
        seen = set(nums[idx:])

        idx = len(set(nums[:idx]))
        cur = k
        while idx:
            cur += 1
            if cur not in seen:
                total += cur
                idx -= 1

        return total


if __name__ == '__main__':
    solu = Solution()
    print(solu.minimalKSum(nums=[1, 4, 25, 10, 25], k=2))
    print(solu.minimalKSum(nums=[5, 6], k=6))

    nums = [
        96, 44, 99, 25, 61, 84, 88, 18, 19, 33, 60, 86, 52, 19, 32, 47, 35, 50,
        94, 17, 29, 98, 22, 21, 72, 100, 40, 84
    ]
    k = 35
    print(solu.minimalKSum(nums, k))  # 794

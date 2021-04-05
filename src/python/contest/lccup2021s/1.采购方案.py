#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1.采购方案.py
@Time    :   2021/04/05 15:00:29
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import bisect
from typing import List


class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = 0
        n = len(nums)
        for i in range(n - 1, 0, -1):
            x = target - nums[i]
            idx = bisect.bisect_right(nums, x, 0, i)
            ans += idx

        return ans % (10**9 + 7)


if __name__ == '__main__':
    solu = Solution()
    print(solu.purchasePlans(nums=[2, 5, 3, 5], target=6))
    print(solu.purchasePlans(nums=[2, 2, 1, 9], target=10))
    print(solu.purchasePlans(nums=[2, 3, 4], target=2))

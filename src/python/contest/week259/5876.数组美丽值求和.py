#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5876.数组美丽值求和.py
@Time    :   2021/09/19 10:32:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        lefts = [0] * (n + 1)
        for i, num in enumerate(nums):
            lefts[i + 1] = max(lefts[i], num)

        rights = [100010] * (n + 1)
        for i in range(n - 1, -1, -1):
            rights[i] = min(rights[i + 1], nums[i])

        ans = 0
        for i in range(1, n - 1):
            if lefts[i] < nums[i] < rights[i + 1]:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.sumOfBeauties(nums=[1, 2, 3]))
    print(solu.sumOfBeauties(nums=[2, 4, 6, 4]))
    print(solu.sumOfBeauties(nums=[3, 2, 1]))

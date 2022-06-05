#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6091.划分数组使最大差为K.py
@Time    :   2022/06/05 10:38:06
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        ans = 1
        j, n = 0, len(nums)
        for i in range(n):
            if nums[i] - nums[j] <= k:
                continue

            ans += 1
            j = i

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.partitionArray(nums=[3, 6, 1, 2, 5], k=2))
    print(solu.partitionArray(nums=[1, 2, 3], k=1))
    print(solu.partitionArray(nums=[2, 2, 4, 5], k=0))

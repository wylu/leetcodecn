#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5227.K次操作后最大化顶端元素.py
@Time    :   2022/03/13 10:54:37
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == 0:
            return -1 if not nums else nums[0]

        if n == 1:
            return -1 if k % 2 else nums[0]

        if k < n:
            return max(max(nums[:k - 1]), nums[k]) if k > 1 else nums[k]
        elif k == n:
            return -1 if not nums[:k - 1] else max(nums[:k - 1])
        else:
            return max(nums)


if __name__ == '__main__':
    solu = Solution()
    print(solu.maximumTop(nums=[5, 2, 2, 4, 0, 6], k=4))
    print(solu.maximumTop(nums=[2], k=1))
    print(solu.maximumTop(nums=[31, 15, 92, 84, 19, 92, 55], k=4))  # 92

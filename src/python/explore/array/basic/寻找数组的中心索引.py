#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   寻找数组的中心索引.py
@Time    :   2020/09/25 23:11:10
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + nums[i]

        for i in range(n):
            if ps[i] == ps[n] - ps[i + 1]:
                return i

        return -1


if __name__ == "__main__":
    solu = Solution()
    print(solu.pivotIndex([1, 7, 3, 6, 5, 6]))
    print(solu.pivotIndex([1, 2, 3]))
    print(solu.pivotIndex([1, -1, 0]))

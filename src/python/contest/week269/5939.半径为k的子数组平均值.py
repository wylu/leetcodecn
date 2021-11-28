#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5939.半径为k的子数组平均值.py
@Time    :   2021/11/28 10:32:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        m = k * 2 + 1
        if m > n:
            return ans

        cur = sum(nums[:m])
        for i in range(k, n - k):
            # print(f'i: {i}, k: {k}, cur: {cur}')
            ans[i] = cur // m
            cur -= nums[i - k]
            if i + k + 1 < n:
                cur += nums[i + k + 1]
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.getAverages(nums=[7, 4, 3, 9, 1, 8, 5, 2, 6], k=3))
    print(solu.getAverages(nums=[100000], k=0))
    print(solu.getAverages(nums=[8], k=100000))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5504.所有排列中的最大和.py
@Time    :   2020/09/19 22:39:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxSumRangeQuery(self, nums: List[int],
                         requests: List[List[int]]) -> int:
        ans, n = 0, len(nums)
        a, d = [0] * n, [0] * n

        for s, e in requests:
            d[s] += 1
            if e + 1 < n:
                d[e + 1] -= 1

        a[0] = d[0]
        for i in range(1, n):
            a[i] = d[i] + a[i - 1]

        a.sort()
        nums.sort()
        for i in range(n - 1, -1, -1):
            if a[i] <= 0:
                break
            ans += a[i] * nums.pop()

        return ans % (10**9 + 7)


if __name__ == '__main__':
    solu = Solution()
    print(solu.maxSumRangeQuery([1, 2, 3, 4, 5], [[1, 3], [0, 1]]))

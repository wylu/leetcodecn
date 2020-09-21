#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5505.使数组和能被P整除.py
@Time    :   2020/09/19 22:47:16
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        ps = [0]
        for i in range(1, n + 1):
            ps.append(ps[-1] + nums[i - 1])

        if ps[-1] % p == 0:
            return 0

        for i in range(1, n):
            j = 0
            while j + i <= n:
                rm = ps[j + i] - ps[j]
                if (ps[n] - rm) % p == 0:
                    return i
                j += 1

        return -1


if __name__ == '__main__':
    solu = Solution()
    print(solu.minSubarray([3, 1, 4, 2], 6))
    print(solu.minSubarray([6, 3, 5, 2], 9))

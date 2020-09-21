#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5504.所有奇数长度子数组的和.py
@Time    :   2020/09/19 22:30:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ps = [0]
        for i in range(1, n + 1):
            ps.append(ps[-1] + arr[i - 1])

        ans = 0
        for i in range(1, n + 1, 2):
            j = 0
            while j + i <= n:
                ans += ps[j + i] - ps[j]
                j += 1

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.sumOddLengthSubarrays([1, 4, 2, 5, 3]))

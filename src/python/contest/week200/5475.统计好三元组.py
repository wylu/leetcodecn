#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5475.统计好三元组.py
@Time    :   2020/08/02 10:31:01
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans, n = 0, len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b
                            and abs(arr[i] - arr[k]) <= c):
                        ans += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3))

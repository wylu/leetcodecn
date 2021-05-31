#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5756.两个数组最小的异或值之和.py
@Time    :   2021/05/30 08:46:02
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        MAX_MASK = 1 << n
        f = [0x7FFFFFFF] * MAX_MASK
        f[0] = 0

        for mask in range(MAX_MASK):
            c = bin(mask).count('1')

            for i in range(n):
                if mask & (1 << i):
                    continue

                next = mask | (1 << i)
                f[next] = min(f[next], f[mask] + (nums1[c] ^ nums2[i]))

        return f[MAX_MASK - 1]


if __name__ == '__main__':
    solu = Solution()
    print(solu.minimumXORSum(nums1=[1, 2], nums2=[2, 3]))
    print(solu.minimumXORSum(nums1=[1, 0, 3], nums2=[5, 3, 4]))

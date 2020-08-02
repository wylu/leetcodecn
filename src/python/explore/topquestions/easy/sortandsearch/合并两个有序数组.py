#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   合并两个有序数组.py
@Time    :   2020/08/02 10:05:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def merge(self, l1: List[int], m: int, l2: List[int], n: int) -> None:
        if not l2:
            return

        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if l1[i] > l2[j]:
                val = l1[i]
                i -= 1
            else:
                val = l2[j]
                j -= 1

            l1[k] = val
            k -= 1

        while j >= 0:
            l1[k] = l2[j]
            k -= 1
            j -= 1


if __name__ == '__main__':
    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]
    solu = Solution()
    solu.merge(nums1, 3, nums2, 3)
    print(nums1)

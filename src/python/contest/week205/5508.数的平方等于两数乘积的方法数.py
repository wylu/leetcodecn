#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5508.数的平方等于两数乘积的方法数.py
@Time    :   2020/09/06 10:42:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def cal(a: List[int], s) -> int:
            cnt, n = 0, len(a)
            for j in range(n - 1):
                for k in range(j + 1, n):
                    val = a[j] * a[k]
                    if val in s:
                        cnt += s[val]
            return cnt

        s1, s2 = {}, {}
        for num in nums1:
            s1[num * num] = s1.get(num * num, 0) + 1
        for num in nums2:
            s2[num * num] = s2.get(num * num, 0) + 1
        return cal(nums1, s2) + cal(nums2, s1)


if __name__ == '__main__':
    solu = Solution()
    print(solu.numTriplets([7, 4], [5, 2, 8, 9]))
    print(solu.numTriplets([1, 1], [1, 1, 1]))
    print(solu.numTriplets([7, 7, 8, 3], [1, 2, 9, 7]))
    print(solu.numTriplets([4, 7, 9, 11, 23], [3, 5, 1024, 12, 18]))

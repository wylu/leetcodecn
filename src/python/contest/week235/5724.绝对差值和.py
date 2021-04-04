#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5724.绝对差值和.py
@Time    :   2021/04/04 10:39:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import bisect
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        ans, diffs = 0, []
        for i in range(n):
            delta = abs(nums1[i] - nums2[i])
            ans += delta
            diffs.append((delta, i))

        diffs.sort(reverse=True)
        opts = nums1[:]
        opts.sort()

        mini = ans
        for delta, i in diffs:
            if delta == 0:
                break

            idx = bisect.bisect_left(opts, nums2[i])
            if idx == n:
                idx -= 1

            tmp = abs(opts[idx] - nums2[i])
            if tmp < delta and (ans - delta + tmp) < mini:
                mini = ans - delta + tmp

            if tmp != 0 and idx > 0:
                tmp = abs(opts[idx - 1] - nums2[i])
                if tmp < delta and (ans - delta + tmp) < mini:
                    mini = ans - delta + tmp

        return mini % (10**9 + 7)


if __name__ == '__main__':
    solu = Solution()
    print(solu.minAbsoluteSumDiff(nums1=[1, 7, 5], nums2=[2, 3, 5]))
    nums1 = [2, 4, 6, 8, 10]
    nums2 = [2, 4, 6, 8, 10]
    print(solu.minAbsoluteSumDiff(nums1, nums2))
    nums1 = [1, 10, 4, 4, 2, 7]
    nums2 = [9, 3, 5, 1, 7, 4]
    print(solu.minAbsoluteSumDiff(nums1, nums2))

    nums1 = [
        56, 51, 39, 1, 12, 14, 58, 82, 18, 41, 70, 64, 18, 7, 44, 90, 55, 23,
        11, 79, 59, 76, 67, 92, 60, 80, 57, 11, 66, 32, 76, 73, 35, 65, 55, 37,
        38, 26, 4, 7, 64, 84, 98, 61, 78, 1, 80, 33, 5, 66, 32, 30, 52, 29, 41,
        2, 21, 83, 30, 35, 21, 30, 13, 26, 36, 93, 81, 41, 98, 23, 20, 19, 45,
        52, 25, 51, 52, 24, 2, 45, 21, 97, 11, 92, 28, 37, 58, 29, 5, 18, 98,
        94, 86, 65, 88, 8, 75, 12, 9, 66
    ]
    nums2 = [
        64, 32, 98, 65, 67, 40, 71, 93, 74, 24, 49, 80, 98, 35, 86, 52, 99, 65,
        15, 92, 83, 84, 80, 71, 46, 11, 26, 70, 80, 2, 81, 57, 97, 12, 68, 10,
        49, 80, 24, 18, 45, 72, 33, 94, 60, 5, 94, 99, 14, 41, 25, 83, 77, 67,
        49, 70, 94, 83, 55, 17, 61, 44, 50, 62, 3, 36, 67, 10, 2, 39, 53, 62,
        44, 72, 66, 7, 3, 6, 80, 38, 43, 100, 17, 25, 24, 78, 8, 4, 36, 86, 9,
        68, 99, 64, 65, 15, 42, 59, 79, 66
    ]
    print(solu.minAbsoluteSumDiff(nums1, nums2))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5500.乘积为正数的最长子数组长度.py
@Time    :   2020/08/30 10:25:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        i, j, n = 0, 0, len(nums)
        while j < n:
            while i < n and nums[i] == 0:
                i += 1
            if i == n:
                break

            j = i
            pos, neg, first_neg, last_neg = 0, 0, -1, -1
            while j < n and nums[j] != 0:
                if nums[j] > 0:
                    pos += 1
                else:
                    neg += 1
                    if first_neg == -1:
                        first_neg = j
                    if first_neg != -1:
                        last_neg = j
                j += 1

            if neg % 2 == 0:
                ans = max(ans, j - i)
            else:
                best = max(j - 1 - first_neg, last_neg - i)
                ans = max(ans, best)

            i = j

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.getMaxLen([1, -2, -3, 4]))
    print(solu.getMaxLen([0, 1, -2, -3, -4]))
    print(solu.getMaxLen([-1, -2, -3, 0, 1]))
    print(solu.getMaxLen([-1, 2]))
    print(solu.getMaxLen([1, 2, 3, 5, -6, 4, 0, 10]))
    print(solu.getMaxLen([1]))
    print(solu.getMaxLen([-1]))
    print(solu.getMaxLen([0]))

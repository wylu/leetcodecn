#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   寻找峰值.py
@Time    :   2020/10/03 11:28:11
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    solu = Solution()
    print(solu.findPeakElement([1, 2, 3, 1]))
    print(solu.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
    print(solu.findPeakElement([1, 2, 3, 4, 5]))
    print(solu.findPeakElement([5, 4, 3, 2, 1]))

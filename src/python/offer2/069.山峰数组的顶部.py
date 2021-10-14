#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   069.山峰数组的顶部.py
@Time    :   2021/10/14 11:42:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :   https://leetcode-cn.com/problems/B1IidL/
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    solu = Solution()
    print(solu.peakIndexInMountainArray([1, 3, 2]))
    print(solu.peakIndexInMountainArray([1, 2]))
    print(solu.peakIndexInMountainArray([2, 1]))
    print(solu.peakIndexInMountainArray([3, 4, 5, 1]))

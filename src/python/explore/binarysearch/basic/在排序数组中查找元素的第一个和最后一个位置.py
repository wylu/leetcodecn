#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   在排序数组中查找元素的第一个和最后一个位置.py
@Time    :   2020/10/03 12:11:11
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x: int) -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            return left

        start = search(target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = search(target + 1)
        return [start, end - 1]


if __name__ == "__main__":
    solu = Solution()
    print(solu.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(solu.searchRange([5, 7, 7, 8, 8, 10], 6))
    print(solu.searchRange([7, 7, 8, 8], 7))
    print(solu.searchRange([7, 7, 8, 8], 8))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   搜索插入位置.py
@Time    :   2020/09/25 23:24:07
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == "__main__":
    solu = Solution()
    print(solu.searchInsert([1, 3, 5, 6], 5))
    print(solu.searchInsert([1, 3, 5, 6], 2))
    print(solu.searchInsert([1, 3, 5, 6], 7))
    print(solu.searchInsert([1, 3, 5, 6], 0))

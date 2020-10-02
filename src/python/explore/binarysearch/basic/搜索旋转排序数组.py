#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   搜索旋转排序数组.py
@Time    :   2020/10/02 23:48:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] < target or target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

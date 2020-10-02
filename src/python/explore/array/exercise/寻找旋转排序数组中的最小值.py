#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   寻找旋转排序数组中的最小值.py
@Time    :   2020/10/02 22:17:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


if __name__ == "__main__":
    solu = Solution()
    print(solu.findMin([3, 4, 5, 1, 2]))
    print(solu.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(solu.findMin([1, 2, 3, 4, 5]))

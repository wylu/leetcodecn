#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   寻找旋转排序数组中的最小值II.py
@Time    :   2020/10/05 00:34:47
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
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]


if __name__ == "__main__":
    solu = Solution()
    print(solu.findMin([1, 3, 5]))
    print(solu.findMin([2, 2, 2, 0, 1]))
    print(solu.findMin([3, 1, 3]))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   最后一个小于目标值的元素的下标.py
@Time    :   2020/08/25 15:51:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


def last_less(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid - 1

    return -1 if nums[left] >= target else left


if __name__ == '__main__':
    print(last_less([1, 3, 5], 4))
    print(last_less([5, 5, 6], 4))
    print(last_less([1, 2, 3], 4))
    print(last_less([1, 2, 3, 3, 4], 4))

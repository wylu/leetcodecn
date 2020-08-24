#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   21.调整数组顺序使奇数位于偶数前面.py
@Time    :   2020/08/24 19:11:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
快慢双指针

定义快慢双指针 fast 和 slow，fast 在前，slow 在后。
fast 的作用是向前搜索奇数位置，slow 的作用是指向下一个奇数应当存放的位置；
fast 向前移动，当它搜索到奇数时，将它和 nums[slow] 交换，此时 slow
向前移动一个位置；重复上述操作，直到 fastt 指向数组末尾 .
"""
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        slow = 0
        for fast in range(len(nums)):
            if nums[fast] % 2 == 1:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        return nums


# class Solution:
#     def exchange(self, nums: List[int]) -> List[int]:
#         if not nums:
#             return nums

#         i, j = 0, len(nums) - 1
#         while i < j:
#             while i < j and nums[i] % 2 == 1:
#                 i += 1
#             while i < j and nums[j] % 2 == 0:
#                 j -= 1
#             nums[i], nums[j] = nums[j], nums[i]

#         return nums

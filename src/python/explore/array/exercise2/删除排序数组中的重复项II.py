#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   删除排序数组中的重复项II.py
@Time    :   2020/10/06 18:38:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j, k = 0, 1
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
                k = 1
            elif k <= 1:
                k += 1
                j += 1
                nums[j] = nums[i]
        return j + 1


if __name__ == "__main__":
    solu = Solution()
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    ans = solu.removeDuplicates(nums)
    print(nums[:ans])

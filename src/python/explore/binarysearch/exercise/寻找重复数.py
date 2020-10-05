#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   寻找重复数.py
@Time    :   2020/10/05 11:25:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    solu = Solution()
    print(solu.findDuplicate([1, 3, 4, 2, 2]))
    print(solu.findDuplicate([3, 1, 3, 4, 2]))

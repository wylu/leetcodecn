#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   45.把数组排成最小的数.py
@Time    :   2020/12/02 21:47:58
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
排序判断规则：

设 nums 任意两数字的字符串格式 x 和 y，则
  - 若 x + y < y + x，则 x < y
  - 若 x + y > y + x，则 x > y
"""
from functools import cmp_to_key
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def cmp(s1: str, s2: str) -> int:
            m, n = s1 + s2, s2 + s1
            if m == n:
                return 0
            return -1 if m < n else 1

        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(cmp))

        return ''.join(nums)


if __name__ == "__main__":
    solu = Solution()
    print(solu.minNumber([3, 30, 34, 5, 9]))
    print(solu.minNumber([10, 2]))
    print(solu.minNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

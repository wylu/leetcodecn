#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5217.将杂乱无章的数字排序.py
@Time    :   2022/03/05 22:34:10
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        arr = []
        for i, num in enumerate(nums):
            num = int(''.join([str(mapping[int(ch)]) for ch in str(num)]))
            arr.append((num, i))

        arr.sort()

        return [nums[i] for _, i in arr]


if __name__ == '__main__':
    solu = Solution()
    mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
    nums = [991, 338, 38]
    print(solu.sortJumbled(mapping, nums))

    mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums = [789, 456, 123]
    print(solu.sortJumbled(mapping, nums))

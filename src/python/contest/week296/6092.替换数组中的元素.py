#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6092.替换数组中的元素.py
@Time    :   2022/06/05 10:50:16
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def arrayChange(self, nums: List[int],
                    operations: List[List[int]]) -> List[int]:
        indices = {v: i for i, v in enumerate(nums)}

        for u, v in operations:
            i = indices[u]
            nums[i] = v

            del indices[u]
            indices[v] = i

        return nums


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 2, 4, 6]
    operations = [[1, 3], [4, 7], [6, 1]]
    print(solu.arrayChange(nums, operations))

    nums = [1, 2]
    operations = [[1, 3], [2, 1], [3, 2]]
    print(solu.arrayChange(nums, operations))

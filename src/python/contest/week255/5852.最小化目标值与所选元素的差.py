#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5852.最小化目标值与所选元素的差.py
@Time    :   2021/08/22 10:38:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        values = set([0])
        for row in mat:
            next_values = set()
            for num in row:
                for v in values:
                    next_values.add(v + num)
            values = next_values

        ans = float('inf')
        for total in values:
            ans = min(ans, abs(total - target))

        return ans


if __name__ == '__main__':
    solu = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    target = 13
    print(solu.minimizeTheDifference(mat, target))

    mat = [[1], [2], [3]]
    target = 100
    print(solu.minimizeTheDifference(mat, target))

    mat = [[1, 2, 9, 8, 7]]
    target = 6
    print(solu.minimizeTheDifference(mat, target))

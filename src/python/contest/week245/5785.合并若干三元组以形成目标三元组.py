#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5785.合并若干三元组以形成目标三元组.py
@Time    :   2021/06/13 11:01:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]],
                      target: List[int]) -> bool:
        vals = []
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                vals.append(t)

        x = y = z = 0
        for a, b, c in vals:
            x = max(x, a)
            y = max(y, b)
            z = max(z, c)

        return [x, y, z] == target


if __name__ == '__main__':
    solu = Solution()
    triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
    target = [2, 7, 5]
    print(solu.mergeTriplets(triplets, target))

    triplets = [[1, 3, 4], [2, 5, 8]]
    target = [2, 5, 8]
    print(solu.mergeTriplets(triplets, target))

    triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
    target = [5, 5, 5]
    print(solu.mergeTriplets(triplets, target))

    triplets = [[3, 4, 5], [4, 5, 6]]
    target = [3, 2, 5]
    print(solu.mergeTriplets(triplets, target))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2.烹饪料理.py
@Time    :   2022/04/16 15:04:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]],
                    attribute: List[List[int]], limit: int) -> int:

        def check(state):
            x, y = 0, 0
            remain = materials[::]
            for i in range(n):
                if (1 << i) & state:
                    x += attribute[i][0]
                    y += attribute[i][1]

                    for j in range(5):
                        if cookbooks[i][j] > remain[j]:
                            return False, 0

                        remain[j] -= cookbooks[i][j]

            return y >= limit, x

        ans, n = -1, len(attribute)
        for state in range(1 << n):
            res, x = check(state)
            if res:
                ans = max(ans, x)

        return ans


if __name__ == '__main__':
    solu = Solution()
    meterials = [3, 2, 4, 1, 2]
    cookbooks = [[1, 1, 0, 1, 2], [2, 1, 4, 0, 0], [3, 2, 4, 1, 0]]
    attribute = [[3, 2], [2, 4], [7, 6]]
    limit = 5
    print(solu.perfectMenu(meterials, cookbooks, attribute, limit))

    meterials = [10, 10, 10, 10, 10]
    cookbooks = [[1, 1, 1, 1, 1], [3, 3, 3, 3, 3], [10, 10, 10, 10, 10]]
    attribute = [[5, 5], [6, 6], [10, 10]]
    limit = 1
    print(solu.perfectMenu(meterials, cookbooks, attribute, limit))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1.无人机方阵.py
@Time    :   2021/09/11 15:00:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]],
                              target: List[List[int]]) -> int:
        counter = defaultdict(int)
        m, n = len(source), len(source[0])
        for i in range(m):
            for j in range(n):
                counter[source[i][j]] += 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if counter[target[i][j]] == 0:
                    ans += 1
                else:
                    counter[target[i][j]] -= 1

        return ans


if __name__ == '__main__':
    solu = Solution()

    source = [[1, 3], [5, 4]]
    target = [[3, 1], [6, 5]]
    print(solu.minimumSwitchingTimes(source, target))

    source = [[1, 2, 3], [3, 4, 5]]
    target = [[1, 3, 5], [2, 3, 4]]
    print(solu.minimumSwitchingTimes(source, target))

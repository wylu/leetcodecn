#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5750.人口最多的年份.py
@Time    :   2021/05/09 10:33:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        ans, cnt = logs[0][0], 1
        for x in range(1950, 2051):
            cur = 0
            for b, d in logs:
                if b <= x < d:
                    cur += 1
                elif x < b:
                    break

            if cur > cnt:
                cnt = cur
                ans = x
        return ans


if __name__ == '__main__':
    solu = Solution()
    logs = [[2025, 2041], [1988, 2007], [2003, 2046], [2045,
                                                       2049], [2025, 2027],
            [2014, 2040], [2014, 2027], [2011, 2027], [1972, 2019]]
    print(solu.maximumPopulation(logs))  # 2025

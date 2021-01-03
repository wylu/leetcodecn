#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5642.大餐计数.py
@Time    :   2021/01/03 10:37:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        cnts = defaultdict(int)
        for num in deliciousness:
            cnts[num] += 1

        ans = 0
        for first in sorted(cnts.keys()):
            for i in range(22):
                second = 2**i - first
                if second not in cnts or second < first:
                    continue

                if first == second:
                    ans += (cnts[first] * (cnts[first] - 1)) // 2
                else:
                    ans += cnts[first] * cnts[second]

        return ans % 1000000007


if __name__ == "__main__":
    solu = Solution()
    deliciousness = [
        149, 107, 1, 63, 0, 1, 6867, 1325, 5611, 2581, 39, 89, 46, 18, 12, 20,
        22, 234
    ]
    print(solu.countPairs(deliciousness))  # 12

    print(solu.countPairs([0, 1]))
    print(solu.countPairs([0, 0, 1]))
    print(solu.countPairs([1, 1, 1]))

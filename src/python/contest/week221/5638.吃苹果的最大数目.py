#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5638.吃苹果的最大数目.py
@Time    :   2020/12/27 10:37:56
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import heapq
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans, rest, n = 0, [], len(apples)

        def eat(i: int) -> int:
            cnt = 0
            while rest and cnt == 0:
                d, a = heapq.heappop(rest)
                if d <= i:
                    continue
                cnt += 1
                a -= 1
                if a > 0:
                    heapq.heappush(rest, (d, a))
            return cnt

        for i in range(n):
            if apples[i] > 0:
                heapq.heappush(rest, (i + days[i], apples[i]))

            ans += eat(i)

        while rest:
            ans += eat(n)
            n += 1

        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.eatenApples([1, 2, 3, 5, 2], [3, 2, 1, 4, 2]))
    print(solu.eatenApples([3, 0, 0, 0, 0, 2], [3, 0, 0, 0, 0, 2]))

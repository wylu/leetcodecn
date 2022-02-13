#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6005.使数组变成交替数组的最少操作数.py
@Time    :   2022/02/13 10:33:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:

    def minimumOperations(self, nums: List[int]) -> int:
        cnts = [defaultdict(int), defaultdict(int)]
        totals = [0, 0]
        for i, num in enumerate(nums):
            cnts[i % 2][num] += 1
            totals[i % 2] += 1

        c1 = [(c, v) for v, c in cnts[0].items()]
        c1.sort(reverse=True)
        c2 = [(c, v) for v, c in cnts[1].items()]
        c2.sort(reverse=True)

        def select(cv1, cv2):
            if not cv1 or not cv2:
                return 0

            cnt1, val1 = cv1[0]
            i, n = 0, len(cv2)
            while i < n and cv2[i][1] == val1:
                i += 1

            if i < n:
                cnt2, _ = cv2[i]
                return totals[0] - cnt1 + totals[1] - cnt2

            return totals[0] - cnt1 + totals[1]

        return min(select(c1, c2), select(c2, c1))


if __name__ == '__main__':
    solu = Solution()
    print(solu.minimumOperations(nums=[3, 1, 3, 2, 4, 3]))
    print(solu.minimumOperations(nums=[1, 2, 2, 2, 2]))

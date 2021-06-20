#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5790.查询差绝对值的最小值.py
@Time    :   2021/06/20 11:38:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minDifference(self, nums: List[int],
                      queries: List[List[int]]) -> List[int]:
        m, n = 100, len(nums)
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for k in range(n):
            for j in range(1, m + 1):
                ps[j][k + 1] = ps[j][k]
            ps[nums[k]][k + 1] += 1

        ans = []
        for lo, hi in queries:
            last = cur = float('inf')
            for k in range(1, m + 1):
                if ps[k][hi + 1] - ps[k][lo] == 0:
                    continue
                if last != float('inf'):
                    cur = min(cur, k - last)
                last = k
            if cur == float('inf'):
                cur = -1
            ans.append(cur)

        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [2, 3], [0, 3]]
    print(solu.minDifference(nums, queries))

    nums = [4, 5, 2, 2, 7, 10]
    queries = [[2, 3], [0, 2], [0, 5], [3, 5]]
    print(solu.minDifference(nums, queries))

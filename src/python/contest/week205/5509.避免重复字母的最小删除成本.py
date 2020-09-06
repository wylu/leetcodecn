#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5509.避免重复字母的最小删除成本.py
@Time    :   2020/09/06 11:00:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        dup = []
        n, c = len(s), 0
        for i in range(1, n):
            j = c + 1
            while j < n and s[j] == s[c]:
                j += 1
            if j > c + 1:
                dup.append((c, j - 1))
            c = j

        ans = 0
        for s, e in dup:
            inteval = cost[s:e + 1]
            ans += sum(inteval) - max(inteval)

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.minCost('abaac', [1, 2, 3, 4, 5]))
    print(solu.minCost("abc", [1, 2, 3]))
    print(solu.minCost("aabaa", [1, 2, 3, 4, 1]))

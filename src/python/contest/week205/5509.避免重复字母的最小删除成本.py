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
贪心

对字符串中每部分连续子串进行如下操作：
（1）获取删除该部分子串的总成本，记为 sum
（2）获取删除该部分子串中某个字符的最大成本，记为 max
（3）则避免重复的最小删除成本为 sum - max

将所有连续子串的最小删除成本加起来即为最终结果。
"""
from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans, n = 0, len(s)
        sm, mx = cost[0], cost[0]
        for i in range(1, n):
            if s[i] != s[i - 1]:
                ans += sm - mx
                sm = cost[i]
                mx = cost[i]
            else:
                sm += cost[i]
                mx = max(mx, cost[i])

        ans += sm - mx
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.minCost('abaac', [1, 2, 3, 4, 5]))
    print(solu.minCost("abc", [1, 2, 3]))
    print(solu.minCost("aabaa", [1, 2, 3, 4, 1]))

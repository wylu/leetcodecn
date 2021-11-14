#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5912.每一个查询的最大美丽值.py
@Time    :   2021/11/13 23:26:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]],
                      queries: List[int]) -> List[int]:
        n = len(items)
        queries = [(val, idx) for idx, val in enumerate(queries)]
        items.sort()
        queries.sort()

        ans = [0] * len(queries)
        cur, max_beauty = 0, 0
        for price, idx in queries:
            while cur < n and items[cur][0] <= price:
                max_beauty = max(max_beauty, items[cur][1])
                cur += 1

            ans[idx] = max_beauty

        return ans


if __name__ == '__main__':
    solu = Solution()
    items = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
    queries = [1, 2, 3, 4, 5, 6]
    print(solu.maximumBeauty(items, queries))

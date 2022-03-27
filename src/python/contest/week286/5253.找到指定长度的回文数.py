#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5253.找到指定长度的回文数.py
@Time    :   2022/03/27 10:39:10
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half = (intLength + 1) // 2
        base = 10**(half - 1)
        upper = 10**half - base

        ans = []
        for query in queries:
            if query > upper:
                ans.append(-1)
                continue

            num = str(base + query - 1)
            if intLength % 2:
                ans.append(int(num + num[::-1][1:]))
            else:
                ans.append(int(num + num[::-1]))

        return ans


if __name__ == '__main__':
    solu = Solution()
    # print(solu.kthPalindrome(queries=[1, 2, 3, 4, 5, 90], intLength=3))
    # print(solu.kthPalindrome(queries=[1, 2, 3, 4, 5, 90, 91], intLength=3))
    # print(solu.kthPalindrome(queries=[2, 4, 6], intLength=4))
    # print(solu.kthPalindrome(queries=[1, 2, 3, 10, 11], intLength=1))

    queries = [
        2, 201429812, 8, 520498110, 492711727, 339882032, 462074369, 9, 7, 6
    ]
    intLength = 1
    print(solu.kthPalindrome(queries, intLength))

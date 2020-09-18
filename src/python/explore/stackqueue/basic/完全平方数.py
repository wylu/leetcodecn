#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   完全平方数.py
@Time    :   2020/09/18 22:07:29
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        dist = 0
        q = deque()
        q.append(0)
        while q:
            dist += 1
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                i, need = 1, n - cur
                while i * i <= need:
                    if i * i == need:
                        return dist
                    q.append(cur + i * i)
                    i += 1
        return -1


if __name__ == '__main__':
    solu = Solution()
    print(solu.numSquares(12))
    print(solu.numSquares(13))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5489.两球之间的磁力.py
@Time    :   2020/08/16 10:50:08
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def ok(mid: int) -> bool:
            cnt = 1
            cur = position[0]

            for i in range(n):
                if (position[i] - cur >= mid):
                    cnt += 1
                    cur = position[i]
                    if cnt >= m:
                        return True

            return False

        lo, hi = 0, position[n - 1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if ok(mid):
                lo = mid + 1
            else:
                hi = mid

        return lo - 1


if __name__ == '__main__':
    solu = Solution()
    print(solu.maxDistance([1, 2, 3, 4, 7], 3))
    print(solu.maxDistance([5, 4, 3, 2, 1, 1000000000], 2))

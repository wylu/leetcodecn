#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6006.拿出最少数目的魔法豆.py
@Time    :   2022/02/13 10:59:11
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:

    def minimumRemoval(self, beans: List[int]) -> int:
        total, n = 0, len(beans)
        cnts = defaultdict(int)
        for num in beans:
            cnts[num] += 1
            total += num

        vc = [(v, c) for v, c in cnts.items()]
        vc.sort()

        ans, cur, cnt = total, 0, 0
        for v, c in vc:
            cnt += c
            fetch = cur + (total - cur - v * c - (n - cnt) * v)
            ans = min(ans, fetch)
            cur += v * c

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.minimumRemoval(beans=[4, 1, 6, 5]))
    print(solu.minimumRemoval(beans=[2, 10, 3, 2]))

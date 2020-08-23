#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5495.圆形赛道上经过次数最多的扇区.py
@Time    :   2020/08/23 10:30:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        cnt = [0] * (n + 1)
        for i in range(1, len(rounds)):
            s, e = rounds[i - 1] + 1, rounds[i]
            while s <= n:
                cnt[s] += 1
                s += 1
            s = 1
            while s <= e:
                cnt[s] += 1
                s += 1

        cnt[rounds[0]] += 1
        maxVal = max(cnt)

        ans = [i for i in range(n + 1) if cnt[i] == maxVal]
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.mostVisited(4, [1, 3, 1, 2]))
    print(solu.mostVisited(3, [3, 2, 1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 3, 1]))

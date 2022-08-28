#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6162.收集垃圾的最少总时间.py
@Time    :   2022/08/28 10:42:06
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        mc = pc = gc = 0
        n = len(garbage)
        for i in range(n - 1, -1, -1):
            for ch in garbage[i]:
                if ch == 'M':
                    mc += 1
                elif ch == 'P':
                    pc += 1
                else:
                    gc += 1

            if i > 0:
                if mc > 0:
                    mc += travel[i - 1]
                if pc > 0:
                    pc += travel[i - 1]
                if gc > 0:
                    gc += travel[i - 1]

        return mc + pc + gc


if __name__ == '__main__':
    solu = Solution()
    garbage = ["G", "P", "GP", "GG"]
    travel = [2, 4, 3]
    print(solu.garbageCollection(garbage, travel))

    garbage = ["MMM", "PGM", "GP"]
    travel = [3, 10]
    print(solu.garbageCollection(garbage, travel))

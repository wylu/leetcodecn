#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5992.基于陈述统计最多好人数.py
@Time    :   2022/01/23 10:48:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)

        def check(state: int) -> bool:
            for i, statement in enumerate(statements):
                for j, value in enumerate(statement):
                    if value == 2:
                        continue

                    pi, pj = (1 << i) & state, (1 << j) & state
                    if value == 0:
                        if pi and pj:
                            return False
                    else:
                        if pi and not pj:
                            return False

            return True

        ans = 0
        for state in range(1, 1 << n):
            if check(state):
                ans = max(ans, bin(state).count('1'))

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.maximumGood(statements=[[2, 1, 2], [1, 2, 2], [2, 0, 2]]))
    print(solu.maximumGood(statements=[[2, 0], [0, 2]]))

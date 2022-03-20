#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6029.射箭比赛中的最大得分.py
@Time    :   2022/03/20 11:04:01
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def maximumBobPoints(self, numArrows: int,
                         aliceArrows: List[int]) -> List[int]:
        n = len(aliceArrows)
        bobArrows, best = [0] * n, 0

        for state in range(1 << n):
            flag, cur, score, remain = True, [0] * n, 0, numArrows
            for i in range(1, n):
                if ((1 << i) & state) == 0:
                    continue

                need = aliceArrows[i] + 1
                if remain < need:
                    flag = False
                    break

                cur[i] = need
                remain -= need
                score += i

            if flag and score > best:
                bobArrows, best = cur, score
                if remain:
                    bobArrows[0] = remain

        return bobArrows


if __name__ == '__main__':
    solu = Solution()
    # numArrows = 9
    # aliceArrows = [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0]
    # print(solu.maximumBobPoints(numArrows, aliceArrows))

    # numArrows = 3
    # aliceArrows = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2]
    # print(solu.maximumBobPoints(numArrows, aliceArrows))

    numArrows = 89
    aliceArrows = [3, 2, 28, 1, 7, 1, 16, 7, 3, 13, 3, 5]
    #             [0, 3,  0, 2, 8, 2, 17, 8, 4, 14, 4, 6]
    #             [21,3,  0, 2, 8, 2, 17, 8, 4, 14, 4, 6]
    print(solu.maximumBobPoints(numArrows, aliceArrows))

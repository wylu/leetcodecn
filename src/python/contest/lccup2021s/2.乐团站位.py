#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2.乐团站位.py
@Time    :   2021/04/05 15:22:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        if num == 1:
            return 1

        idx = min(xPos, yPos, num - xPos - 1, num - yPos - 1)
        total = 0
        if idx:
            an = 4 * (num - 1)
            a1 = an - 8 * (idx - 1)
            total = (a1 + an) * idx // 2

        sX = sY = idx
        eX = eY = num - idx - 1
        edge = eX - sX
        if xPos == sX and yPos <= eY:
            total += yPos - sY + 1
        elif xPos <= eX and yPos == eY:
            total += edge + xPos - sX + 1
        elif xPos == eX and yPos < eY:
            total += edge * 2 + eY - yPos + 1
        else:
            total += edge * 3 + eX - xPos + 1

        return total % 9 if total % 9 else 9


if __name__ == '__main__':
    solu = Solution()
    print(solu.orchestraLayout(5, 2, 3))
    print(solu.orchestraLayout(5, 4, 1))
    print(solu.orchestraLayout(5, 3, 0))
    print(solu.orchestraLayout(5, 1, 4))
    print(solu.orchestraLayout(5, 2, 2))
    print(solu.orchestraLayout(4, 0, 0))
    print(solu.orchestraLayout(4, 0, 1))
    print(solu.orchestraLayout(4, 0, 3))
    print(solu.orchestraLayout(4, 1, 1))
    print(solu.orchestraLayout(4, 2, 2))
    print(solu.orchestraLayout(4, 3, 3))
    print(solu.orchestraLayout(3, 0, 0))
    print(solu.orchestraLayout(3, 1, 0))
    print(solu.orchestraLayout(3, 1, 1))
    print(solu.orchestraLayout(3, 2, 2))

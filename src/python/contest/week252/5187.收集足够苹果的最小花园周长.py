#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5187.收集足够苹果的最小花园周长.py
@Time    :   2021/08/01 12:04:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def count(x: int) -> int:
            tot = (x + x) * 4 + x * 4
            gap = (1 + (x - 1)) * (x - 1) // 2 + x * (x - 1)
            tot += gap * 8
            return tot

        ps = [0]
        x = 1
        while ps[-1] < neededApples:
            cnt = count(x)
            ps.append(ps[x - 1] + cnt)
            x += 1

        return (x - 1) * 2 * 4


if __name__ == '__main__':
    solu = Solution()
    print(solu.minimumPerimeter(neededApples=1))
    print(solu.minimumPerimeter(neededApples=13))
    print(solu.minimumPerimeter(neededApples=1000000000))

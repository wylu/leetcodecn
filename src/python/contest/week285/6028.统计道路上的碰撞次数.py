#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6028.统计道路上的碰撞次数.py
@Time    :   2022/03/20 10:40:46
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def countCollisions(self, directions: str) -> int:
        ans = 0
        stk = []
        for d in directions:
            if (not stk or stk[-1] == d or (stk[-1] == 'L' and d == 'R')
                    or (stk[-1] == 'L' and d == 'S')
                    or (stk[-1] == 'S' and d == 'R')):
                stk.append(d)
                continue

            if stk[-1] == 'S' or d == 'S':
                ans += 1
            else:
                ans += 2
            stk.pop()

            while stk and stk[-1] == 'R':
                stk.pop()
                ans += 1

            stk.append('S')

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.countCollisions("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"))  # 20
    # 1 + 2 + 1 + 1 + 1 + 1 + 1 + 2

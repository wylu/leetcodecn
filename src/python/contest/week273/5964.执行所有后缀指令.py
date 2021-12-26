#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5964.执行所有后缀指令.py
@Time    :   2021/12/26 10:32:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int],
                            s: str) -> List[int]:
        c2d = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

        ans = []
        m = len(s)
        sx, sy = startPos
        for i in range(m):
            cnt = 0
            x, y = sx, sy
            for j in range(i, m):
                dx, dy = c2d[s[j]]
                x, y = x + dx, y + dy
                if x < 0 or x >= n or y < 0 or y >= n:
                    break
                cnt += 1

            ans.append(cnt)

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.executeInstructions(n=3, startPos=[0, 1], s="RRDDLU"))
    # print(solu.executeInstructions(n=3, startPos=[0, 1], s=""))

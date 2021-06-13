#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5787.最佳运动员的比拼回合.py
@Time    :   2021/06/13 11:26:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :

f[n][a][b][Min/Max] 表示当前有 n 个运动员站一排，前一个最佳运动员站在第 a 个
位置，后一个最佳运动员站在第 b 个位置，他们相遇的 Min/Max 轮次
"""
from typing import List


class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int,
                          secondPlayer: int) -> List[int]:
        f = [[[[-1, -1] for _ in range(n + 1)] for _ in range(n + 1)]
             for _ in range(n + 1)]

        def solve(n, a, b, r):
            if a == n + 1 - b:
                f[n][a][b][0] = f[n][a][b][1] = r
                return

            if f[n][a][b][0] != -1:
                return

            xVx = xVy = xVz = yVy = yVz = 0
            for i in range(1, n + 1):
                if i == a or i == b:
                    continue
                j = n + 1 - i
                if j == a or j == b:
                    continue
                if i == j:
                    continue

                if i < a and j < a:
                    xVx += 1
                if i < a and a < j < b:
                    xVy += 1
                if i < a and b < j:
                    xVz += 1
                if a < i < b and a < j < b:
                    yVy += 1
                if a < i < b and b < j:
                    yVz += 1

            m = (n + 1) // 2
            bx = by = 0
            if n % 2 == 1 and m < a:
                bx = 1
            if n % 2 == 1 and a < m < b:
                by = 1

            xVx //= 2
            yVy //= 2
            for i in range(xVy + 1):
                for j in range(xVz + 1):
                    for k in range(yVz + 1):
                        pre = xVx + i + j + bx
                        mid = (xVy - i) + yVy + k + by
                        na = pre + 1
                        nb = na + mid + 1
                        solve(m, na, nb, r + 1)
                        if (f[n][a][b][0] == -1
                                or f[m][na][nb][0] < f[n][a][b][0]):
                            f[n][a][b][0] = f[m][na][nb][0]
                        if (f[n][a][b][1] == -1
                                or f[m][na][nb][1] > f[n][a][b][1]):
                            f[n][a][b][1] = f[m][na][nb][1]

        solve(n, firstPlayer, secondPlayer, 1)
        return f[n][firstPlayer][secondPlayer]


if __name__ == '__main__':
    solu = Solution()
    print(solu.earliestAndLatest(n=11, firstPlayer=2, secondPlayer=4))
    print(solu.earliestAndLatest(n=5, firstPlayer=1, secondPlayer=5))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5811.用三种不同颜色为网格涂色.py
@Time    :   2021/07/11 21:15:33
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :

一列一列地填，一次填 m 个格子。
dp[i][s] 表示填好了前 i 列，第 i 列的颜色状况为 s 的方案数。
s 的方案数理论上至多有 3 ^ 5 = 243 种，但是因为相邻的格子的颜色不能相同，
所以 s 满足条件的方案数小于 243。

状态转移方程：
dp[i][s] = \sum_{ps} dp[i-1][ps],  ps|s 符合题目要求   # noqa W605
"""


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        dig = [1, 3, 9, 27, 81, 243]
        max_state = 3**m
        ava = [False] * max_state
        edges = [[] for _ in range(max_state)]
        dp = [[0] * max_state for _ in range(n)]

        def get(state: int, k: int) -> int:
            return (state % dig[k + 1]) // dig[k]

        for s in range(max_state):
            flag = True
            for i in range(1, m):
                if get(s, i - 1) == get(s, i):
                    flag = False
                    break
            ava[s] = flag

        for s in range(max_state):
            if not ava[s]:
                continue
            for ns in range(max_state):
                if not ava[ns]:
                    continue
                flag = True
                for i in range(m):
                    if get(s, i) == get(ns, i):
                        flag = False
                        break
                if flag:
                    edges[s].append(ns)

        for s in range(max_state):
            if ava[s]:
                dp[0][s] = 1

        for i in range(1, n):
            for s in range(max_state):
                for ns in edges[s]:
                    dp[i][ns] = (dp[i][ns] + dp[i - 1][s]) % MOD

        ans = 0
        for s in range(max_state):
            ans += dp[n - 1][s]

        return ans % MOD


if __name__ == '__main__':
    solu = Solution()
    print(solu.colorTheGrid(m=1, n=1))
    print(solu.colorTheGrid(m=1, n=2))
    print(solu.colorTheGrid(m=5, n=5))

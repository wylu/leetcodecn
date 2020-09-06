#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5492.分割字符串的方案数.py
@Time    :   2020/09/05 22:35:17
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7

        n = len(s)
        cnt = sum(1 for c in s if c == '1')
        if cnt % 3 != 0:
            return 0
        if cnt == 0:
            return ((1 + (n - 2)) * (n - 2) // 2) % MOD

        part = cnt // 3
        idx, cur = [], 0
        for i in range(n):
            if s[i] == '1':
                if cur == 0:
                    idx.append([i])
                cur += 1

            if cur == part:
                idx[-1].append(i)
                cur = 0

        return (idx[1][0] - idx[0][1]) * (idx[2][0] - idx[1][1]) % MOD


if __name__ == '__main__':
    solu = Solution()
    print(solu.numWays('10101'))
    print(solu.numWays('1001'))
    print(solu.numWays('0000'))
    print(solu.numWays('100100010100110'))
    print(solu.numWays('00000'))
    print(solu.numWays('00000000'))

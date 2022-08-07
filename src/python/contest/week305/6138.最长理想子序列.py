#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6138.最长理想子序列.py
@Time    :   2022/08/07 10:57:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :

f[i][j]: 对于字符串 s[0...i] 以 chr(ord('a')+j) 为结尾的理想字符串的最长子序列的长度
"""


class Solution:

    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)

        f = [[0] * 26 for _ in range(n)]
        f[0][ord(s[0]) - ord('a')] = 1

        for i in range(1, n):
            for j in range(0, 26):
                f[i][j] = f[i - 1][j]

            ch = ord(s[i]) - ord('a')

            start = max(0, ch - k)
            end = min(25, ch + k)

            # print(f'{s[i]} [{start}, {end}]: {f[i-1]}')

            for j in range(start, end + 1):
                f[i][ch] = max(f[i][ch], f[i - 1][j] + 1)

        return max(f[n - 1])


if __name__ == '__main__':
    solu = Solution()
    print(solu.longestIdealString(s="acfgbd", k=2))
    print(solu.longestIdealString(s="abcd", k=3))
    print(solu.longestIdealString(s="eduktdb", k=15))

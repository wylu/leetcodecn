#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   19.秋叶收藏集.py
@Time    :   2020/09/16 23:41:08
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
Dynamic Programming

State:
  f[i][0]: 表示将前 i 个字符变成形如 'r...' 的形式需要的最小调整次数
  f[i][1]: 表示将前 i 个字符变成形如 'r...y...' 的形式需要的最小调整次数
  f[i][2]: 表示将前 i 个字符变成形如 'r...y...r...' 的形式需要的最小调整次数
"""


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        f = [[0] * 3 for _ in range(n)]
        f[0][0] = 0 if leaves[0] == 'r' else 1

        for i in range(1, n):
            f[i][0] = f[i - 1][0] + (0 if leaves[i] == 'r' else 1)
            f[i][1] = f[i - 1][0] + (0 if leaves[i] == 'y' else 1)

            if i > 1:
                f[i][1] = min(f[i][1],
                              f[i - 1][1] + (0 if leaves[i] == 'y' else 1))
                f[i][2] = f[i - 1][1] + (0 if leaves[i] == 'r' else 1)

            if i > 2:
                f[i][2] = min(f[i][2],
                              f[i - 1][2] + (0 if leaves[i] == 'r' else 1))

        return f[n - 1][2]


if __name__ == '__main__':
    solu = Solution()
    print(solu.minimumOperations('rrryyyrryyyrr'))
    print(solu.minimumOperations('rrr'))
    print(solu.minimumOperations('yyy'))
    print(solu.minimumOperations('yrr'))
    print(solu.minimumOperations('rry'))
    print(solu.minimumOperations('yry'))

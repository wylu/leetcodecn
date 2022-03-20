#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6023.用地毯覆盖后的最少白色砖块.py
@Time    :   2022/03/20 18:25:04
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :

一般来说，题目求什么就定义什么：定义 f[i][j] 表示用 i 条地毯覆盖前 j 块板砖时，
没被覆盖的白色砖块的最少数目。

转移时可以考虑是否用第 i 条地毯的末尾覆盖第 j 块板砖：

不覆盖：f[i][j] = f[i][j-1] + [floor[j]='1']
覆盖：f[i][j] = f[i-1][j-carpetLen]
取二者最小值。

注意 i=0 的时候只能不覆盖，需要单独计算。

最后答案为 f[numCarpets][floor.length-1]
"""


class Solution:

    def minimumWhiteTiles(self, floor: str, numCarpets: int,
                          carpetLen: int) -> int:
        n = len(floor)
        f = [[0] * n for _ in range(numCarpets + 1)]
        f[0][0] = int(floor[0])
        for i in range(1, n):
            f[0][i] = f[0][i - 1] + int(floor[i])

        for i in range(1, numCarpets + 1):
            # i条地毯能完美覆盖前 carpetLen * i 块地板，
            # 所以 j < carpetLen * i 的 f[i][j] 均为 0
            for j in range(carpetLen * i, n):
                f[i][j] = min(f[i][j - 1] + int(floor[j]),
                              f[i - 1][j - carpetLen])

        return f[numCarpets][n - 1]

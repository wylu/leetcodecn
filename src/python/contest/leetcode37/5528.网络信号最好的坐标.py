#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5528.网络信号最好的坐标.py
@Time    :   2020/10/17 22:35:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import math
from typing import List


class Solution:
    def bestCoordinate(self, towers: List[List[int]],
                       radius: int) -> List[int]:
        minx = miny = 0x7FFFFFFF
        maxx = maxy = -0x8FFFFFFF
        for x, y, _ in towers:
            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, x)
            maxy = max(maxy, y)

        ans = []
        power = 0
        for i in range(minx, maxx + 1):
            for j in range(miny, maxy + 1):
                tot = 0
                for x, y, q in towers:
                    d = math.sqrt((x - i)**2 + (y - j)**2)
                    if d <= radius:
                        tot += math.floor(q / (1 + d))

                if tot > power:
                    ans = [[i, j]]
                    power = tot
                elif tot == power:
                    ans.append([i, j])

        ans.sort()
        return ans[0]


if __name__ == "__main__":
    solu = Solution()
    towers = [[3, 46, 2], [3, 27, 46], [7, 25, 50], [32, 39, 3], [4, 42, 37],
              [20, 18, 48], [13, 16, 23], [22, 36, 24], [40, 7, 26],
              [16, 21, 1], [46, 33, 34], [19, 11, 19], [31, 22, 41],
              [37, 29, 20], [18, 29, 28], [36, 0, 45], [39, 22, 37],
              [25, 25, 45], [0, 31, 15], [44, 45, 13], [18, 47, 23],
              [47, 19, 26], [48, 18, 32]]
    print(solu.bestCoordinate(towers, 44))

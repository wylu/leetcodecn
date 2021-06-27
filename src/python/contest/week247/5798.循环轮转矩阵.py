#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5798.循环轮转矩阵.py
@Time    :   2021/06/27 10:31:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        def rotate(start, offset):
            sx = sy = start
            ex, ey = m - start - 1, n - start - 1
            tmp = []
            for i in range(sy, ey + 1):
                tmp.append(grid[sx][i])

            if ex > sx:
                for i in range(sx + 1, ex + 1):
                    tmp.append(grid[i][ey])

                if ey > sy:
                    for i in range(ey - 1, sy - 1, -1):
                        tmp.append(grid[ex][i])

                    if ex - sx > 1:
                        for i in range(ex - 1, sx, -1):
                            tmp.append(grid[i][sx])

            tmp = tmp[offset:] + tmp[:offset]
            j = 0

            for i in range(sy, ey + 1):
                grid[sx][i] = tmp[j]
                j += 1

            if ex > sx:
                for i in range(sx + 1, ex + 1):
                    grid[i][ey] = tmp[j]
                    j += 1

                if ey > sy:
                    for i in range(ey - 1, sy - 1, -1):
                        grid[ex][i] = tmp[j]
                        j += 1

                    if ex - sx > 1:
                        for i in range(ex - 1, sx, -1):
                            grid[i][sx] = tmp[j]
                            j += 1

        # print(m, n)
        for start in range(min(m, n) // 2):
            circle = (n - start * 2) * 2 + (m - (start + 1) * 2) * 2
            offset = k % circle
            # print(circle, offset)
            rotate(start, offset)

        return grid


if __name__ == '__main__':
    solu = Solution()
    # grid = [[40, 10], [30, 20]]
    # k = 1
    # print(solu.rotateGrid(grid, k))

    # grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    # k = 2
    # print(solu.rotateGrid(grid, k))

    grid = [
        [3970, 1906, 3608, 298, 3072, 3546, 1502, 773, 4388, 3115, 747, 3937],
        [2822, 304, 4179, 1780, 1709, 1058, 3645, 681, 2910, 2513, 4357, 1038],
        [4471, 2443, 218, 550, 2766, 4780, 1997, 1672, 4095, 161, 4645, 3838],
        [
            2035, 2350, 3653, 4127, 3208, 4717, 4347, 3452, 1601, 3725, 3060,
            2270
        ],
        [188, 2278, 81, 3454, 3204, 1897, 2862, 4381, 3704, 2587, 743, 3832],
        [996, 4499, 66, 2742, 1761, 1189, 608, 509, 2344, 3271, 3076, 108],
        [
            3274, 2042, 2157, 3226, 2938, 3766, 2610, 4510, 219, 1276, 3712,
            4143
        ],
        [744, 234, 2159, 4478, 4161, 4549, 4214, 4272, 701, 4376, 3110, 4896],
        [4431, 1011, 757, 2690, 83, 3546, 946, 1122, 2216, 3944, 2715, 2842],
        [898, 4087, 703, 4153, 3297, 2968, 3268, 4717, 1922, 2527, 3139, 1516],
        [1086, 1090, 302, 1273, 2292, 234, 3268, 2284, 4203, 3838, 2227, 3651],
        [2055, 4406, 2278, 3351, 3217, 2506, 4525, 233, 3829, 63, 4470, 3170],
        [
            3797, 3276, 1755, 1727, 1131, 4108, 3633, 1835, 1345, 1293, 2778,
            2805
        ],
        [1215, 84, 282, 2721, 2360, 2321, 1435, 2617, 1202, 2876, 3420, 3034]
    ]
    k = 405548684
    print(solu.rotateGrid(grid, k))

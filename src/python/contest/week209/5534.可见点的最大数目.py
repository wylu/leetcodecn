#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5534.可见点的最大数目.py
@Time    :   2020/10/04 10:52:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import math
from typing import List


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int,
                      location: List[int]) -> int:
        n = len(points)
        dx, dy = 0 - location[0], 0 - location[1]
        for i in range(n):
            points[i][0] += dx
            points[i][1] += dy

        ans = 0
        for d in range(360):
            start, end = d - angle / 2, d + angle / 2
            start = (start + 360) % 360
            end = (end + 360) % 360

            cnt = 0
            for x, y in points:
                theta = (math.atan2(x, y) * 180 / math.pi + 360) % 360
                if start > end:
                    if theta >= start or theta <= end:
                        cnt += 1
                else:
                    if start <= theta <= end or (x == 0 and y == 0):
                        cnt += 1

            ans = max(ans, cnt)

        return ans


if __name__ == "__main__":
    solu = Solution()
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [1, 2], [2, 1]]
    print(solu.visiblePoints(points, 0, [1, 1]))

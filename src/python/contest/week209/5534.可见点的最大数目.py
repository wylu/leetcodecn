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
        x, y = location
        same = 0
        v = []
        for px, py in points:
            if px == x and py == y:
                same += 1
            else:
                theta = math.atan2(px - x, py - y) * 180 / math.pi
                v.append((theta + 360) % 360)

        v.sort()
        m = len(v)
        for i in range(m):
            v.append(v[i] + 360)

        cnt, right, n = 0, 0, len(v)
        for left in range(m):
            while right + 1 < n and v[right + 1] - v[left] <= angle:
                right += 1
            cnt = max(cnt, right - left + 1)

        return same + cnt


if __name__ == "__main__":
    solu = Solution()
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [1, 2], [2, 1]]
    print(solu.visiblePoints(points, 0, [1, 1]))

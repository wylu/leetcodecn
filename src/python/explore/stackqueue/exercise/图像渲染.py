#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   图像渲染.py
@Time    :   2020/09/21 23:41:29
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image

        d = (0, 1, 0, -1, 0)
        n, m, origin = len(image), len(image[0]), image[sr][sc]

        def dfs(x: int, y: int) -> None:
            if x < 0 or x >= n or y < 0 or y >= m or image[x][y] != origin:
                return
            image[x][y] = newColor
            for i in range(4):
                dfs(x + d[i], y + d[i + 1])

        dfs(sr, sc)
        return image


if __name__ == '__main__':
    solu = Solution()
    print(solu.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))

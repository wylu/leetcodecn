#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6059.检查是否有合法括号字符串路径.py
@Time    :   2022/05/08 11:44:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from functools import lru_cache
from typing import List


class Solution:

    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(x: int, y: int, cnt: int) -> bool:
            if x >= m or y >= n:
                return False

            if grid[x][y] == '(':
                cnt += 1
            else:
                if cnt == 0:
                    return False
                cnt -= 1

            if x == m - 1 and y == n - 1:
                return cnt == 0

            return dfs(x + 1, y, cnt) or dfs(x, y + 1, cnt)

        return dfs(0, 0, 0)


if __name__ == '__main__':
    solu = Solution()
    grid = [["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]
    print(solu.hasValidPath(grid))

    grid = [[")", ")"], ["(", "("]]
    print(solu.hasValidPath(grid))

    grid = [["(", ")"], ["(", ")"]]
    print(solu.hasValidPath(grid))

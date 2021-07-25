#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5825.最大兼容性评分和.py
@Time    :   2021/07/25 11:03:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]],
                            mentors: List[List[int]]) -> int:
        ans = 0
        n = len(mentors)
        m = len(mentors[0])
        used = [False] * n
        cnts = {}
        for i in range(n):
            for j in range(n):
                c = 0
                for k in range(m):
                    if students[i][k] == mentors[j][k]:
                        c += 1
                cnts[(i, j)] = c

        def dfs(i: int, tot: int) -> None:
            nonlocal ans
            if i == n:
                ans = max(ans, tot)
                return

            for j in range(n):
                if not used[j]:
                    used[j] = True
                    dfs(i + 1, tot + cnts[(i, j)])
                    used[j] = False

        dfs(0, 0)
        return ans

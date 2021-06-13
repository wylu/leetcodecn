#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5786.可移除字符的最大数目.py
@Time    :   2021/06/13 10:36:37
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        m, n = len(s), len(p)

        def check(k):
            mark = [True] * m
            for i in range(k):
                mark[removable[i]] = False

            i = j = 0
            while i < m and j < n:
                if mark[i] and s[i] == p[j]:
                    j += 1
                i += 1

            return j == n

        left, right = 0, len(removable)
        while left < right:
            k = (left + right + 1) // 2
            if check(k):
                left = k
            else:
                right = k - 1

        return left


if __name__ == '__main__':
    solu = Solution()
    print(solu.maximumRemovals(s="abcacb", p="ab", removable=[3, 1, 0]))

    s = "abcbddddd"
    p = "abcd"
    removable = [3, 2, 1, 4, 5, 6]
    print(solu.maximumRemovals(s, p, removable))

    s = "abcab"
    p = "abc"
    removable = [0, 1, 2, 3, 4]
    print(solu.maximumRemovals(s, p, removable))

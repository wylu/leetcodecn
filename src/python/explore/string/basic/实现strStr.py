#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   实现strStr.py
@Time    :   2020/10/02 15:51:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def strStr(self, s: str, p: str) -> int:
        if not p:
            return 0

        n = len(p)
        fail = [-1] * n
        k, j = -1, 0
        while j < n - 1:
            if k == -1 or p[k] == p[j]:
                k += 1
                j += 1
                fail[j] = k
            else:
                k = fail[k]

        m = len(s)
        i, j = 0, 0
        while i < m and j < n:
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = fail[j]

        return i - j if j == n else -1


if __name__ == "__main__":
    solu = Solution()
    print(solu.strStr("hello", "ll"))
    print(solu.strStr("aaaaa", "bba"))
    print(solu.strStr("", "a"))

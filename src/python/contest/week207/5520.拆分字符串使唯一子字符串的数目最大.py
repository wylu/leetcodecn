#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5520.拆分字符串使唯一子字符串的数目最大.py
@Time    :   2020/09/20 10:37:01
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans = 0
        n, cache = len(s), set()

        def dfs(c: int) -> None:
            nonlocal ans
            if c == n:
                ans = max(ans, len(cache))
                return
            for size in range(1, n - c + 1):
                tmp = s[c:c + size]
                if tmp in cache:
                    continue
                cache.add(tmp)
                dfs(c + size)
                cache.remove(tmp)

        dfs(0)
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.maxUniqueSplit("ababccc"))
    print(solu.maxUniqueSplit("aba"))
    print(solu.maxUniqueSplit("aa"))
    print(solu.maxUniqueSplit("a"))
    print(solu.maxUniqueSplit("addbsd"))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   38.字符串的排列.py
@Time    :   2020/09/03 20:07:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        def dfs(c: int) -> None:
            if c == n:
                ans.append(''.join(s))
                return

            used = set()
            for i in range(c, n):
                if s[i] in used:
                    continue
                used.add(s[i])
                s[c], s[i] = s[i], s[c]
                dfs(c + 1)
                s[c], s[i] = s[i], s[c]

        ans = []
        s, n = list(s), len(s)
        dfs(0)
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.permutation('abc'))
    print(solu.permutation('aac'))

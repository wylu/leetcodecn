#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5237.得到回文串的最少操作次数.py
@Time    :   2022/03/05 23:18:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import Counter


class Solution:

    def minMovesToMakePalindrome(self, s: str) -> int:
        ans = 0

        opts = Counter(s)
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue

            step, char, ni, nj = 0x7FFFFFFF, None, None, None
            for opt, cnt in opts.items():
                if cnt == 0 or cnt == 1:
                    continue

                p, q = i, j
                while p < j and s[p] != opt:
                    p += 1
                while q > i and s[q] != opt:
                    q -= 1

                need = (p - i) + (j - q)
                if need < step:
                    step, char, ni, nj = need, opt, p, q

            if char:
                opts[char] -= 2
                ch = s[ni]
                for k in range(ni - 1, i - 1, -1):
                    s[k + 1] = s[k]
                s[i] = ch

                ch = s[nj]
                for k in range(nj, j):
                    s[k] = s[k + 1]
                s[j] = ch

                ans += step

            i += 1
            j -= 1

        # print(''.join(s))
        return ans


if __name__ == '__main__':
    solu = Solution()
    # print(solu.minMovesToMakePalindrome(s="aabb"))
    # print(solu.minMovesToMakePalindrome(s="letelt"))
    print(solu.minMovesToMakePalindrome(s="sdttfdlsgfl"))  # 13
    """
    sdttfdlsgfl
    sdttfdlgfls 3
    sdttflgflds 4

    sdfttlglfds 3
    sdflttglfds 2
    sdfltgtlfds 1

    13

    sdlttfgflds 3
    """

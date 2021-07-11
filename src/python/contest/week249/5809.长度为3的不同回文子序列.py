#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5809.长度为3的不同回文子序列.py
@Time    :   2021/07/11 10:31:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        n = len(s)

        lefts = [set() for _ in range(n)]
        rights = [set() for _ in range(n)]

        for i in range(1, n - 1):
            lefts[i] |= lefts[i - 1]
            lefts[i].add(s[i - 1])

        for i in range(n - 2, 0, -1):
            rights[i] |= rights[i + 1]
            rights[i].add(s[i + 1])

        # print(f'lefts: {lefts}\nrights: {rights}')

        seen = set()

        for i in range(1, n - 1):
            opts = lefts[i] & rights[i]
            for ch in opts:
                opt = ''.join([ch, s[i], ch])
                if opt not in seen:
                    ans += 1
                    seen.add(opt)

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.countPalindromicSubsequence(s="aabca"))
    print(solu.countPalindromicSubsequence(s="adc"))
    print(solu.countPalindromicSubsequence(s="bbcbaba"))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6099.小于等于K的最长二进制子序列.py
@Time    :   2022/06/19 11:10:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def longestSubsequence(self, s: str, k: int) -> int:
        cnt, n = 0, len(s)
        state = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                ns = state | (1 << (n - i - 1))
                if ns <= k:
                    cnt += 1
                    state = ns
            else:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solu = Solution()
    print(solu.longestSubsequence(s="1001010", k=5))
    print(solu.longestSubsequence(s="00101001", k=1))

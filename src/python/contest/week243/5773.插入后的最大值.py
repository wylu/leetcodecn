#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5773.插入后的最大值.py
@Time    :   2021/05/30 10:35:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def maxValue(self, s: str, x: int) -> str:
        n = len(s)
        x = str(x)

        if s[0] == '-':
            for i in range(1, n):
                if x < s[i]:
                    return s[:i] + x + s[i:]
            return s + x

        for i in range(n):
            if x > s[i]:
                return s[:i] + x + s[i:]
        return s + x


if __name__ == '__main__':
    solu = Solution()
    print(solu.maxValue("99", 9))
    print(solu.maxValue("-13", 2))
    print(solu.maxValue("28824579515", 8))

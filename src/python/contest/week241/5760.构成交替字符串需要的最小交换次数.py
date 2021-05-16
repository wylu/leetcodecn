#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5760.构成交替字符串需要的最小交换次数.py
@Time    :   2021/05/16 10:34:59
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        c0 = c1 = 0
        for ch in s:
            if ch == '0':
                c0 += 1
            else:
                c1 += 1

        if abs(c0 - c1) > 1:
            return -1

        n = len(s)

        def count(ch1: str, ch2: str) -> int:
            tot, p1, p2 = 0, 0, 1
            while True:
                while p1 < n and s[p1] == ch1:
                    p1 += 2

                while p2 < n and s[p2] == ch2:
                    p2 += 2

                if (p1 >= n and p2 < n) or (p1 < n and p2 >= n):
                    return 0x7FFFFFFF
                if (p1 >= n and p2 >= n):
                    break

                tot += 1
                p1 += 2
                p2 += 2

            return tot

        return min(count('0', '1'), count('1', '0'))


if __name__ == '__main__':
    solu = Solution()
    print(solu.minSwaps('111000'))
    print(solu.minSwaps('010'))
    print(solu.minSwaps('1110'))
    print(solu.minSwaps('0'))
    print(solu.minSwaps('1'))
    print(solu.minSwaps('110100'))
    print(solu.minSwaps('1101000'))
    print(solu.minSwaps('100'))
    print(solu.minSwaps('001'))

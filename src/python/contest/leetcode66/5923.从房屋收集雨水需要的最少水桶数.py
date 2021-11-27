#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5923.从房屋收集雨水需要的最少水桶数.py
@Time    :   2021/11/27 22:33:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def minimumBuckets(self, street: str) -> int:
        n = len(street)
        street = list(street)
        for i in range(n):
            if street[i] != 'H':
                continue
            if i - 1 > 0 and street[i - 1] == 'B':
                continue
            if i == n - 1 or street[i + 1] == 'H':
                if i == 0 or (i - 1 > 0 and street[i - 1] != '.'):
                    return -1
                street[i - 1] = 'B'
            else:
                street[i + 1] = 'B'

        ans = 0
        for ch in street:
            if ch == 'B':
                ans += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.minimumBuckets(street="H..H"))
    print(solu.minimumBuckets(street=".H.H."))
    print(solu.minimumBuckets(street=".HHH."))
    print(solu.minimumBuckets(street="H"))
    print(solu.minimumBuckets(street="."))

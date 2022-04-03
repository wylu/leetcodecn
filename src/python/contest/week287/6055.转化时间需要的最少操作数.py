#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6055.转化时间需要的最少操作数.py
@Time    :   2022/04/03 10:30:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def convertTime(self, current: str, correct: str) -> int:
        a, b = current.split(':')
        cu = int(a) * 60 + int(b)

        a, b = correct.split(':')
        co = int(a) * 60 + int(b)

        gap = co - cu
        if co < cu:
            gap += 24 * 60

        ans = 0
        for opt in (60, 15, 5, 1):
            d, gap = divmod(gap, opt)
            ans += d

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.convertTime(current="02:30", correct="04:35"))
    print(solu.convertTime(current="11:00", correct="11:01"))
    print(solu.convertTime(current="11:00", correct="11:00"))
    print(solu.convertTime(current="11:00", correct="01:16"))

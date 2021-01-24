#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5661.替换隐藏数字得到的最晚时间.py
@Time    :   2021/01/24 10:30:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        p = list(time)
        if time[:2] == '??':
            p[0] = '2'
            p[1] = '3'
        elif p[0] == '?':
            p[0] = '1' if p[1] > '3' else '2'
        elif p[1] == '?':
            p[1] = '3' if p[0] > '1' else '9'

        if p[-2] == '?':
            p[-2] = '5'
        if p[-1] == '?':
            p[-1] = '9'

        return ''.join(p)


if __name__ == "__main__":
    solu = Solution()
    print(solu.maximumTime('??:3?'))

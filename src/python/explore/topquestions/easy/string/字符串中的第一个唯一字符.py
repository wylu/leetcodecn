#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   字符串中的第一个唯一字符.py
@Time    :   2020/07/29 12:42:08
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = [[0, -1] for _ in range(26)]

        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if cnt[idx][0] == 0:
                cnt[idx][1] = i
            cnt[idx][0] += 1

        first = -1
        for c, p in cnt:
            if c == 1:
                first = p if first == -1 else min(first, p)

        return first

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   有效的字母异位词.py
@Time    :   2020/07/29 23:40:29
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = [0 for _ in range(26)]

        for c in s:
            i = ord(c) - ord('a')
            cnt[i] += 1

        for c in t:
            i = ord(c) - ord('a')
            cnt[i] -= 1

        for c in cnt:
            if c != 0:
                return False

        return True

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5804.检查是否所有字符出现次数相同.py
@Time    :   2021/07/24 22:30:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        pre = 0
        for c in cnt:
            if c != 0:
                if pre == 0:
                    pre = c
                    continue

                if c != pre:
                    return False

        return True

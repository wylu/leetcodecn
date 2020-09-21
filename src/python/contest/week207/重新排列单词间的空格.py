#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   重新排列单词间的空格.py
@Time    :   2020/09/20 10:30:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        for ch in text:
            if ch == ' ':
                spaces += 1

        text = text.split()
        n = len(text) - 1
        if n == 0:
            return ''.join(text) + ' ' * spaces

        gap, res = spaces // n, spaces % n
        return (' ' * gap).join(text) + (' ' * res)

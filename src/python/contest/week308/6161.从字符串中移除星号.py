#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6161.从字符串中移除星号.py
@Time    :   2022/08/28 10:39:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def removeStars(self, s: str) -> str:
        stk = []
        for ch in s:
            if ch != '*':
                stk.append(ch)
            else:
                stk.pop()
        return ''.join(stk)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   反转字符串.py
@Time    :   2020/07/29 10:02:11
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        if not s:
            return

        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6074.字母在字符串中的百分比.py
@Time    :   2022/05/22 10:30:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

from collections import Counter


class Solution:

    def percentageLetter(self, s: str, letter: str) -> int:
        return int(Counter(s)[letter] / len(s) * 100)

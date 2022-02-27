#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6008.统计包含给定前缀的字符串.py
@Time    :   2022/02/27 10:30:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(int(word.startswith(pref)) for word in words)

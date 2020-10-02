#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   反转字符串中的单词III.py
@Time    :   2020/10/02 22:03:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(w[::-1] for w in s.split())

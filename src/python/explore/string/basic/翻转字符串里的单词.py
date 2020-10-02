#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   翻转字符串里的单词.py
@Time    :   2020/10/02 15:05:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

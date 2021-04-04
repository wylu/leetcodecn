#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5722.截断句子.py
@Time    :   2021/04/04 10:30:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])

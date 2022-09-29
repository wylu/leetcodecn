#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   01.09.字符串轮转.py
@Time    :   2022/09/29 15:07:40
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s2 in (s1 + s1)

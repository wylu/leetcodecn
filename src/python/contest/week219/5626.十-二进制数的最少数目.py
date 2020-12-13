#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5626.十-二进制数的最少数目.py
@Time    :   2020/12/13 10:34:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(num) for num in n)

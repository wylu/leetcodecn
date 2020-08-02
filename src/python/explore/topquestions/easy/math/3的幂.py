#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   3的幂.py
@Time    :   2020/08/02 23:27:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 3^19 = 1162261467 < (2^31 - 1)
        return n > 0 and 1162261467 % n == 0

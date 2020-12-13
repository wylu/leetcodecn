#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5625.比赛中的配对次数.py
@Time    :   2020/12/13 10:30:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            ans += n // 2
            n = n // 2 + n % 2
        return ans

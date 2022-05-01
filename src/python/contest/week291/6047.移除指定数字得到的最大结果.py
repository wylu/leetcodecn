#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6047.移除指定数字得到的最大结果.py
@Time    :   2022/05/01 10:30:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def removeDigit(self, number: str, digit: str) -> str:
        ans = 0
        indices = [i for i, d in enumerate(number) if d == digit]
        for idx in indices:
            num = int(number[:idx] + number[idx + 1:])
            ans = max(ans, num)
        return str(ans)

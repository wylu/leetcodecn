#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5902.检查句子中的数字是否递增.py
@Time    :   2021/10/17 10:30:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        cur = 0
        for p in s.split():
            if p.isdigit():
                p = int(p)
                if p <= cur:
                    return False
                cur = p
        return True

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6078.重排字符形成目标字符串.py
@Time    :   2022/05/29 10:30:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import Counter


class Solution:

    def rearrangeCharacters(self, s: str, target: str) -> int:
        c1 = Counter(s)
        c2 = Counter(target)

        ans = 0
        while True:
            flag = True
            for k, v in c2.items():
                if k not in c1 or c1[k] < v:
                    flag = False
                    break
                c1[k] -= v

            if not flag:
                break

            ans += 1

        return ans

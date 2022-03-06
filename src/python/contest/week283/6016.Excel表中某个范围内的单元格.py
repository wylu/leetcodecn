#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6016.Excel表中某个范围内的单元格.py
@Time    :   2022/03/06 10:30:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def cellsInRange(self, s: str) -> List[str]:
        rs, re = int(s[1]), int(s[-1])
        cs, ce = ord(s[0]) - ord('A'), ord(s[-2]) - ord('A')

        ans = []
        for c in range(cs, ce + 1):
            ch = chr(c + ord('A'))
            for r in range(rs, re + 1):
                ans.append(f'{ch}{r}')

        return ans

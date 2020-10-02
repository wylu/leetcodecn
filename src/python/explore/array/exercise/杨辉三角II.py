#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   杨辉三角II.py
@Time    :   2020/10/02 19:16:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = [1]
        for i in range(1, rowIndex + 1):
            cur = [1]
            for j in range(1, i):
                cur.append(pre[j - 1] + pre[j])
            cur.append(1)
            pre = cur
        return pre

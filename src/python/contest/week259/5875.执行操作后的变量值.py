#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5875.执行操作后的变量值.py
@Time    :   2021/09/19 10:30:37
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for oper in operations:
            if oper[0] == '+' or oper[-1] == '+':
                x += 1
            else:
                x -= 1
        return x

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5963.反转两次的数字.py
@Time    :   2021/12/26 10:30:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return int(str(int(str(num)[::-1]))[::-1]) == num

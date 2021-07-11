#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5808.数组串联.py
@Time    :   2021/07/11 10:30:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

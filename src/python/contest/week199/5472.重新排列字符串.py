#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5472.重新排列字符串.py
@Time    :   2020/07/26 11:22:29
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ns = ['' for _ in range(len(s))]
        for i in range(len(s)):
            ns[indices[i]] = s[i]
        return ''.join(ns)

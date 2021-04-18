#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5734.判断句子是否为全字母句.py
@Time    :   2021/04/18 10:30:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        flag = [False] * 26
        for ch in sentence:
            flag[ord(ch) - ord('a')] = True
        return all(flag)

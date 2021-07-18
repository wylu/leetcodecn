#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5161.可以输入的最大单词数.py
@Time    :   2021/07/18 10:30:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        words = text.split()
        brokenLetters = set(list(brokenLetters))
        for word in words:
            flag = True
            for ch in word:
                if ch in brokenLetters:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans

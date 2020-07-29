#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   验证回文字符串.py
@Time    :   2020/07/29 23:44:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if i < j:
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False

        return True

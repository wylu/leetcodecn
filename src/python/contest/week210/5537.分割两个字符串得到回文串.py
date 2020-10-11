#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5537.分割两个字符串得到回文串.py
@Time    :   2020/10/11 10:41:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def isPalindrome(s: str) -> bool:
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        if isPalindrome(a) or isPalindrome(b):
            return True

        n = len(a)
        return a[0] == b[n - 1] or a[n - 1] == b[0]

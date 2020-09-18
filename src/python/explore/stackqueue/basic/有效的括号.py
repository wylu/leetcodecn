#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   有效的括号.py
@Time    :   2020/09/18 22:45:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        brackets = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            elif not stack or stack.pop() != brackets[c]:
                return False

        return not stack

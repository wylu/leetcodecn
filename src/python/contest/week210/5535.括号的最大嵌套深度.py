#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5535.括号的最大嵌套深度.py
@Time    :   2020/10/11 10:30:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        ans, cnt = 0, 0
        for ch in s:
            if ch == '(':
                cnt += 1
            elif ch == ')':
                ans = max(ans, cnt)
                cnt -= 1
        return ans

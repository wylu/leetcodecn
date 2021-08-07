#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5193.删除字符使字符串变好.py
@Time    :   2021/08/07 23:49:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        if not s:
            return 0

        ans = [s[0]]
        cnt = 1
        for i in range(1, len(s)):
            if s[i] != ans[-1]:
                ans.append(s[i])
                cnt = 1
            elif cnt < 2:
                ans.append(s[i])
                cnt += 1

        return ''.join(ans)

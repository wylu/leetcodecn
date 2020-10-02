#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   最长公共前缀.py
@Time    :   2020/10/02 14:06:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        ans = strs[0]
        for i in range(1, len(strs)):
            cur = strs[i]
            j, n = 0, min(len(ans), len(cur))
            while j < n and ans[j] == cur[j]:
                j += 1

            ans = ans[:j]
            if not ans:
                break

        return ans

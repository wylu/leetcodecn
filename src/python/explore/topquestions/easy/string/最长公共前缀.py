#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   最长公共前缀.py
@Time    :   2020/07/31 23:07:08
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, ws: List[str]) -> str:
        if not ws:
            return ''

        prefix = []
        minLen = len(ws[0])
        for s in ws:
            if len(s) < minLen:
                minLen = len(s)

        for i in range(minLen):
            c = ws[0][i]
            flag = False
            for s in ws:
                if s[i] != c:
                    flag = True
                    break
            if flag:
                break
            prefix.append(c)

        return ''.join(prefix)


if __name__ == '__main__':
    solu = Solution()
    print(solu.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solu.longestCommonPrefix(["dog", "racecar", "car"]))

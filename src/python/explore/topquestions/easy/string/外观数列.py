#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   外观数列.py
@Time    :   2020/07/31 12:48:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'

        for _ in range(1, n):
            i, ns, tmp = 0, len(s), []

            while i < ns:
                j, cnt = i, 0
                while j < ns and s[j] == s[i]:
                    cnt += 1
                    j += 1

                tmp.append(str(cnt))
                tmp.append(s[i])
                i = j

            s = ''.join(tmp)

        return s

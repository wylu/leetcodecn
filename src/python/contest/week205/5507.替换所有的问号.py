#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5507.替换所有的问号.py
@Time    :   2020/09/06 10:30:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s)
        s = list(s)

        for i in range(n):
            if s[i] != '?':
                continue
            used = []
            if i > 0:
                used.append(ord(s[i - 1]) - ord('a'))
            if i < n - 1 and s[i + 1] != '?':
                used.append(ord(s[i + 1]) - ord('a'))

            for j in range(26):
                if j not in used:
                    s[i] = chr(j + ord('a'))
                    break

        return ''.join(s)


if __name__ == '__main__':
    solu = Solution()
    print(solu.modifyString('??yw?ipkj?'))

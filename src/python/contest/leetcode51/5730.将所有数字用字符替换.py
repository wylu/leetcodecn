#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5730.将所有数字用字符替换.py
@Time    :   2021/05/01 22:31:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        for i in range(1, len(s), 2):
            s[i] = chr(ord(s[i - 1]) + int(s[i]))
        return ''.join(s)


if __name__ == '__main__':
    solu = Solution()
    print(solu.replaceDigits(s="a1c1e1"))
    print(solu.replaceDigits(s="a1b2c3d4e"))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   字符串转换整数(atoi).py
@Time    :   2020/07/29 23:57:10
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        s = s.strip()
        if not s or (s[0] != '-' and s[0] != '+' and not s[0].isdigit()):
            return 0

        sign = 1 if s[0] != '-' else -1
        if s[0] == '-' or s[0] == '+':
            s = s[1:]

        MAX_INT32, MIN_INT32 = (1 << 31) - 1, -(1 << 31)
        MAX = (1 << 31) - 1 if sign == 1 else (1 << 31)

        ans = 0
        for c in s:
            if not c.isdigit():
                break

            c = ord(c) - ord('0')
            if ans > MAX // 10 or (ans == MAX // 10 and c > MAX % 10):
                return MAX_INT32 if sign == 1 else MIN_INT32

            ans = ans * 10 + c

        return sign * ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.myAtoi('42'))
    print(solu.myAtoi('   -42'))
    print(solu.myAtoi('4193 with words'))
    print(solu.myAtoi('words and 987'))
    print(solu.myAtoi('-91283472332'))

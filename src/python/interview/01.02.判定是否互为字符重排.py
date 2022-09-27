#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   01.02.判定是否互为字符重排.py
@Time    :   2022/09/27 20:50:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def CheckPermutation(self, s1: str, s2: str) -> bool:
        c = [0] * 26
        for ch in s1:
            c[ord(ch) - ord('a')] += 1
        for ch in s2:
            c[ord(ch) - ord('a')] -= 1
        return not any(c)


if __name__ == '__main__':
    solu = Solution()
    print(solu.CheckPermutation("abc", "bca"))
    print(solu.CheckPermutation("abc", "bad"))

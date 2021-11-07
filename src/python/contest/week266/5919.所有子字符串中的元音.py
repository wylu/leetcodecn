#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5919.所有子字符串中的元音.py
@Time    :   2021/11/07 10:38:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        ans = 0
        for i, ch in enumerate(word):
            if ch in 'aeiou':
                ans += (i + 1) * (n - i)
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.countVowels(word="aba"))
    print(solu.countVowels(word="abc"))
    print(solu.countVowels(word="ltcd"))
    print(solu.countVowels(word="noosabasboosa"))

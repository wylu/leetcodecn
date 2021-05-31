#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5772.检查某单词是否等于两单词之和.py
@Time    :   2021/05/30 10:30:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str,
                   targetWord: str) -> bool:
        def str2num(word: str) -> int:
            res = 0
            for ch in word:
                res = res * 10 + ord(ch) - ord('a')
            return res

        return str2num(firstWord) + str2num(secondWord) == str2num(targetWord)


if __name__ == '__main__':
    solu = Solution()
    print(solu.isSumEqual(firstWord="acb", secondWord="cba", targetWord="cdb"))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5867.反转单词前缀.py
@Time    :   2021/09/12 10:30:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word
        return word[:idx + 1][::-1] + word[idx + 1:]


if __name__ == '__main__':
    solu = Solution()
    print(solu.reversePrefix(word="abcdefd", ch="d"))

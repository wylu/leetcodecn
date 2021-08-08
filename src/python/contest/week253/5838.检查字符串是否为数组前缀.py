#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5838.检查字符串是否为数组前缀.py
@Time    :   2021/08/08 10:30:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        while s and words:
            if not s.startswith(words[0]):
                return False
            s = s[len(words[0]):]
            words = words[1:]
        return s == ''


if __name__ == '__main__':
    solu = Solution()

    s = "iloveleetcode"
    words = ["i", "love", "leetcode", "apples"]
    print(solu.isPrefixString(s, words))

    s = "iloveleetcode"
    words = ["apples", "i", "love", "leetcode"]
    print(solu.isPrefixString(s, words))

    s = "a"
    words = ["aa", "aaaa", "banana"]
    print(solu.isPrefixString(s, words))

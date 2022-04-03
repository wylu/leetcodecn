#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5302.加密解密字符串.py
@Time    :   2022/04/03 10:58:16
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Encrypter:

    def __init__(self, keys: List[str], values: List[str],
                 dictionary: List[str]):
        self.k2v = {k: v for k, v in zip(keys, values)}
        self.cnt = defaultdict(int)
        for word in dictionary:
            self.cnt[self.encrypt(word)] += 1

    def encrypt(self, word1: str) -> str:
        return ''.join([self.k2v[k] for k in word1])

    def decrypt(self, word2: str) -> int:
        return self.cnt[word2]


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)

if __name__ == '__main__':
    encrypter = Encrypter(
        keys=['a', 'b', 'c', 'd'],
        values=["ei", "zf", "ei", "am"],
        dictionary=[
            "abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"
        ],
    )
    print(encrypter.encrypt("abcd"))
    print(encrypter.decrypt("eizfeiam"))

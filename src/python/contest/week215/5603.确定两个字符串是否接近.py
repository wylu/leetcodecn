#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5603.确定两个字符串是否接近.py
@Time    :   2020/11/15 10:51:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1, n2 = len(word1), len(word2)
        if n1 != n2:
            return False

        cnt1, cnt2 = defaultdict(int), defaultdict(int)
        for ch in word1:
            cnt1[ch] += 1
        for ch in word2:
            cnt2[ch] += 1

        vals1 = list(cnt1.values()).sort()
        vals2 = list(cnt2.values()).sort()
        if vals1 != vals2:
            return False

        return cnt1.keys() == cnt2.keys()


if __name__ == "__main__":
    solu = Solution()
    print(solu.closeStrings("cabbba", "abbccc"))
    print(solu.closeStrings("uau", "ssx"))
    print(solu.closeStrings("aaa", "bbb"))

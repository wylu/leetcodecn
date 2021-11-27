#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5922.统计出现过一次的公共字符串.py
@Time    :   2021/11/27 22:30:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1, cnt2 = defaultdict(int), defaultdict(int)
        for word in words1:
            cnt1[word] += 1
        for word in words2:
            cnt2[word] += 1

        ans = 0
        for word in cnt1.keys():
            if cnt1[word] == 1 and cnt2[word] == 1:
                ans += 1
        return ans

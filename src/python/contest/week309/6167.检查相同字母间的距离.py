#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6167.检查相同字母间的距离.py
@Time    :   2022/09/04 10:30:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def checkDistances(self, s: str, distance: List[int]) -> bool:
        indices = {}
        for i, ch in enumerate(s):
            if ch not in indices:
                indices[ch] = i
                continue
            j = indices[ch]
            k = ord(ch) - ord('a')
            if distance[k] != i - j - 1:
                return False
        return True


if __name__ == '__main__':
    solu = Solution()
    s = "abaccb"
    distance = [
        1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0
    ]
    print(solu.checkDistances(s, distance))

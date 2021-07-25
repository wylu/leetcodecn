#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5806.描述绘画结果.py
@Time    :   2021/07/24 23:13:58
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import heapq
from typing import List


class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == '__main__':
    solu = Solution()
    segments = [[1, 4, 5], [4, 7, 7], [1, 7, 9]]
    print(solu.splitPainting(segments))

    segments = [[1, 7, 9], [6, 8, 15], [8, 10, 7]]
    print(solu.splitPainting(segments))

    segments = [[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]]
    print(solu.splitPainting(segments))

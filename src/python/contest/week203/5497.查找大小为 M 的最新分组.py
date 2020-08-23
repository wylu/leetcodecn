#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5497.查找大小为 M 的最新分组.py
@Time    :   2020/08/23 11:09:07
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        s, e, o = '1' * m + '0', '0' + '1' * m, '0' + '1' * m + '0'
        n = len(arr)
        cur = '0' * n
        ans = -1
        for i, v in enumerate(arr):
            cur = cur[:v] + '1' + cur[v + 1:]
            if cur.startswith(s) or cur.endswith(e) or cur.find(o) != -1:
                ans = i + 1

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.findLatestStep([3, 5, 1, 2, 4], 1))
    print(solu.findLatestStep([3, 5, 1, 2, 4], 2))
    print(solu.findLatestStep([1], 1))
    print(solu.findLatestStep([2, 1], 2))

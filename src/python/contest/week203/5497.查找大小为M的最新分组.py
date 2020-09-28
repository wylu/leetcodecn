#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5497.查找大小为M的最新分组.py
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
        n = len(arr)
        es = [(-1, -1)] * (n + 1)
        ans, cnt = -1, 0

        for i in range(n):
            left = right = arr[i]

            if arr[i] > 1 and es[arr[i] - 1][0] != -1:
                left = es[arr[i] - 1][0]
                llen = es[arr[i] - 1][1] - es[arr[i] - 1][0] + 1
                if llen == m:
                    cnt -= 1

            if arr[i] < n and es[arr[i] + 1][0] != -1:
                right = es[arr[i] + 1][1]
                rlen = es[arr[i] + 1][1] - es[arr[i] + 1][0] + 1
                if rlen == m:
                    cnt -= 1

            nlen = right - left + 1
            if nlen == m:
                cnt += 1

            if cnt > 0:
                ans = i + 1

            es[left] = es[right] = (left, right)

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.findLatestStep([3, 5, 1, 2, 4], 1))
    print(solu.findLatestStep([3, 5, 1, 2, 4], 2))
    print(solu.findLatestStep([1], 1))
    print(solu.findLatestStep([2, 1], 2))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5499.重复至少K次且长度为M的模式.py
@Time    :   2020/08/30 10:25:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n - m + 1):
            cnt = 0
            for j in range(i, n - m + 1, m):
                flag = True
                for z in range(m):
                    if arr[i + z] != arr[j + z]:
                        flag = False
                        break
                if flag:
                    cnt += 1
                else:
                    break
            if cnt >= k:
                return True

        return False


if __name__ == '__main__':
    solu = Solution()
    print(solu.containsPattern([1, 2, 4, 4, 4, 4], 1, 3))
    print(solu.containsPattern([1, 2, 1, 2, 1, 1, 1, 3], 2, 2))
    print(solu.containsPattern([1, 2, 1, 2, 1, 3], 2, 3))
    print(solu.containsPattern([1, 2, 3, 1, 2], 2, 2))
    print(solu.containsPattern([2, 2, 2, 2], 2, 3))
    print(solu.containsPattern([2, 2, 1, 2, 2, 1, 1, 1, 2, 1], 2, 2))

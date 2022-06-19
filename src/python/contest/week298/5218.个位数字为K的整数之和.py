#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5218.个位数字为K的整数之和.py
@Time    :   2022/06/19 10:34:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from functools import lru_cache


class Solution:

    def minimumNumbers(self, num: int, k: int) -> int:

        @lru_cache(None)
        def dfs(num: int) -> int:
            if num == 0:
                return 0
            if num == k:
                return 1
            if (num % 2 != 0 and k % 2 == 0) or num < k:
                return -1

            res, c = 0x7FFFFFFF, k
            while c + 10 <= num:
                c += 10

            while c >= 0:
                if num - c == num:
                    c -= 10
                    continue
                s = dfs(num - c)
                if s == -1:
                    c -= 10
                    continue
                res = min(res, 1 + s)
                c -= 10

            return -1 if res == 0x7FFFFFFF else res

        return dfs(num)


if __name__ == '__main__':
    solu = Solution()
    print(solu.minimumNumbers(num=58, k=9))
    print(solu.minimumNumbers(num=37, k=2))
    print(solu.minimumNumbers(num=0, k=7))

    print(solu.minimumNumbers(num=3000, k=7))
    print(solu.minimumNumbers(num=3000, k=1))

    print(solu.minimumNumbers(num=4, k=0))
    print(solu.minimumNumbers(num=10, k=0))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5933.k镜像数字的和.py
@Time    :   2021/11/21 10:53:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        dat = [
            0, 9, 9, 90, 90, 900, 900, 9000, 9000, 90000, 90000, 900000,
            900000, 9000000, 9000000, 90000000, 90000000, 900000000, 900000000,
            9000000000
        ]

        def check(num: int) -> bool:
            res = []
            while num:
                res.append(num % k)
                num //= k

            i, j = 0, len(res) - 1
            while i < j:
                if res[i] != res[j]:
                    return False
                i += 1
                j -= 1
            return True

        def find(n: int) -> int:
            k = 1
            while n > dat[k]:
                n -= dat[k]
                k += 1

            size = (k + 1) >> 1
            base = pow(10, size - 1)
            base += n - 1

            half = str(base)
            if k % 2 == 0:
                res = half + half[::-1]
            else:
                res = half + half[:-1][::-1]

            return int(res) if half else 0

        ans = 0
        cur = 0
        while n:
            cur += 1
            num = find(cur)
            if check(num):
                ans += num
                n -= 1

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.kMirror(k=2, n=5))
    print(solu.kMirror(k=3, n=7))
    print(solu.kMirror(k=7, n=17))

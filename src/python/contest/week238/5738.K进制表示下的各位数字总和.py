#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5738.K进制表示下的各位数字总和.py
@Time    :   2021/04/25 10:30:29
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n > 1:
            ans += n % k
            n //= k

        if n:
            ans += n

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.sumBase(34, 6))
    print(solu.sumBase(10, 10))
    print(solu.sumBase(5, 2))
    print(solu.sumBase(5, 10))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   计数质数.py
@Time    :   2020/08/02 22:45:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
欧拉线性筛法

基本思路:
任意一个合数（2 不是合数），都可以表示成素数的乘积。
每个合数必有一个最小素因子，如果每个合数都用最小素因子筛去，那个这个合数就不会
被重复标记筛去，所以算法为线性时间复杂度。

例如合数 30 = 2 * 3 * 5 ，这个合数一定是被最小素因子 2 筛去的。
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # 元素值为 True 表示该元素下标值为素数
        mark = [True for _ in range(n)]
        primes = []
        for i in range(2, n):
            if mark[i]:
                primes.append(i)

            j, lp = 0, len(primes)
            while j < lp and i * primes[j] < n:
                mark[i * primes[j]] = False

                if i % primes[j] == 0:
                    break

                j += 1

        ans = 0
        for i in range(2, n):
            if mark[i]:
                ans += 1

        return ans

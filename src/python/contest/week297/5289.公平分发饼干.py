#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5289.公平分发饼干.py
@Time    :   2022/06/12 11:02:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k >= len(cookies):
            return max(cookies)

        n = len(cookies)
        state = 0

        def check(mid: int, k: int) -> bool:
            nonlocal state
            if k == 0:
                return state == (1 << n) - 1

            opt, cnt = 0, 0
            for s in range(1 << n):
                if s & state != 0:
                    continue

                cur = 0
                for i in range(n):
                    if (1 << i) & s:
                        cur += cookies[i]

                if cnt < cur <= mid:
                    opt, cnt = s, cur

            state |= opt
            return check(mid, k - 1)

        lt, rt = 0, 10**6
        while lt < rt:
            state, mid = 0, lt + (rt - lt) // 2

            if check(mid, k):
                rt = mid
            else:
                lt = mid + 1

        return lt


if __name__ == '__main__':
    solu = Solution()
    cookies = [8, 15, 10, 20, 8]
    k = 2
    print(solu.distributeCookies(cookies, k))

    cookies = [6, 1, 3, 2, 2, 4, 1, 2]
    k = 3
    print(solu.distributeCookies(cookies, k))

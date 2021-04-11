#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5727.找出游戏的获胜者.py
@Time    :   2021/04/11 10:32:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k == 1:
            return n

        ans = list(range(1, n + 1))
        cnt, cur = n - 1, 0
        while cnt:
            tmp = 0
            while tmp < k:
                cur %= n
                if ans[cur] != 0:
                    tmp += 1
                cur += 1

            ans[cur - 1] = 0
            cnt -= 1

        for num in ans:
            if num:
                return num


if __name__ == '__main__':
    solu = Solution()
    print(solu.findTheWinner(5, 2))
    print(solu.findTheWinner(6, 5))
    print(solu.findTheWinner(3, 1))
    print(solu.findTheWinner(5, 3))

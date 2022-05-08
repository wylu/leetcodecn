#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6058.统计打字方案数.py
@Time    :   2022/05/08 10:39:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :

2 a
22 aa/b
222 aaa/ab/ba/c
2222 | 2 + a | 22 + b | 222 + c | = 1 + 2 + 3 = 7 aaaa/aab/aba/ac baa/bb ca

7 p
77 pp/q
777 ppp/pq/qp/r
7777 pppp/ppq/pqp/pr qpp/qq rp s = 8
"""
from collections import deque


class Solution:

    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        if n < 2:
            return 1

        pressedKeys += '#'
        MOD = 10**9 + 7
        ans = 1
        que = deque([1])
        for i in range(1, n + 1):
            if (pressedKeys[i] != pressedKeys[i - 1]):
                ans = (ans * que[-1]) % MOD
                que = deque([1])
                continue

            m = len(que)
            if (m < 3 or (m < 4 and
                          (pressedKeys[i] == '7' or pressedKeys[i] == '9'))):
                que.append(que[-1] * 2)
            else:
                cur = que[-1] + que[-2] + que[-3]
                if pressedKeys[i] == '7' or pressedKeys[i] == '9':
                    cur += que[-4]
                que.append(cur)
                que.popleft()

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.countTexts(pressedKeys="22233"))
    print(solu.countTexts(pressedKeys="222222222222222222222222222222222222"))
    print(solu.countTexts(pressedKeys="2222"))
    print(solu.countTexts(pressedKeys="7777"))
    print(solu.countTexts(pressedKeys="9999"))
    print(solu.countTexts(pressedKeys="444479999555588866"))  # 3136

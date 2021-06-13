#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5770.反转表达式值的最少操作次数.py
@Time    :   2021/06/12 23:30:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def minOperationsToFlip(self, s: str) -> int:
        n = len(s)
        pre = [-1] * n
        stk = []
        for i in range(n):
            if s[i] == '(':
                stk.append(i)
            elif s[i] == ')':
                pre[i] = stk.pop()

        def dfs(L, R):
            if L == R:
                return (0, 1) if s[L] == '0' else (1, 0)

            if s[R] == ')' and pre[R] == L:
                return dfs(L + 1, R - 1)

            M = pre[R] - 1 if s[R] == ')' else R - 1
            LL = dfs(L, M - 1)
            RR = dfs(M + 1, R)

            zero = min(LL[0] + RR[0], LL[0] + RR[1] + int(s[M] == '|'),
                       LL[1] + RR[0] + int(s[M] == '|'))
            one = min(LL[1] + RR[1], LL[0] + RR[1] + int(s[M] == '&'),
                      LL[1] + RR[0] + int(s[M] == '&'))
            return zero, one

        return max(dfs(0, n - 1))


if __name__ == '__main__':
    solu = Solution()
    print(solu.minOperationsToFlip("1&(0|1)"))
    print(solu.minOperationsToFlip("(0&0)&(0&0&0)"))
    print(solu.minOperationsToFlip("(0|(1|0&1))"))

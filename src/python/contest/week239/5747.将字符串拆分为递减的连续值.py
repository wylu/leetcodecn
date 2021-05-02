#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5747.将字符串拆分为递减的连续值.py
@Time    :   2021/05/02 10:33:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        stk = []

        def dfs(c: int) -> bool:
            if c == n:
                return len(stk) >= 2

            num = 0
            for i in range(c, n):
                num = num * 10 + int(s[i])
                if not stk:
                    stk.append(num)
                    if dfs(i + 1):
                        return True
                    stk.pop()
                else:
                    if num >= stk[-1]:
                        return False

                    if stk[-1] - num == 1:
                        stk.append(num)
                        if dfs(i + 1):
                            return True
                        stk.pop()

            return False

        return dfs(0)


if __name__ == '__main__':
    solu = Solution()
    # print(solu.splitString(s="123"))
    # print(solu.splitString(s="0201"))
    # print(solu.splitString(s="321"))
    print(solu.splitString(s="1234"))
    print(solu.splitString(s="050043"))
    print(solu.splitString(s="9080701"))
    print(solu.splitString(s="10009998"))

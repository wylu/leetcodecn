#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5765.跳跃游戏VII.py
@Time    :   2021/05/23 11:11:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False

        n = len(s)
        stk = [0]
        for i in range(n):
            if s[i] == '1':
                continue

            m = len(stk) - 1
            while m >= 0:
                if stk[m] + minJump <= i <= stk[m] + maxJump:
                    stk.append(i)
                    break
                m -= 1

        return stk[-1] == n - 1


if __name__ == '__main__':
    solu = Solution()
    print(solu.canReach(s="011010", minJump=2, maxJump=3))
    print(solu.canReach(s="01101110", minJump=2, maxJump=3))
    print(solu.canReach(s="01011010", minJump=2, maxJump=5))
    print(solu.canReach(s="0000000000", minJump=2, maxJump=5))

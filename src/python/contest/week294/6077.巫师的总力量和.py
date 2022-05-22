#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6077.巫师的总力量和.py
@Time    :   2022/05/22 17:43:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from itertools import accumulate
from typing import List


class Solution:

    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)

        # left[i] 为左侧严格小于 strength[i] 的最近元素位置（不存在时为 -1）
        # right[i] 为右侧小于等于 strength[i] 的最近元素位置（不存在时为 n）
        left, right, stk = [-1] * n, [n] * n, []
        for i, v in enumerate(strength):
            while stk and strength[stk[-1]] >= v:
                right[stk.pop()] = i
            if stk:
                left[i] = stk[-1]
            stk.append(i)

        # 前缀和的前缀和
        ss = list(accumulate(accumulate(strength, initial=0), initial=0))

        ans, MOD = 0, 10**9 + 7
        for i, v in enumerate(strength):
            l, r = left[i] + 1, right[i] - 1  # [l, r]  左闭右闭
            tot = ((i - l + 1) * (ss[r + 2] - ss[i + 1]) - (r - i + 1) *
                   (ss[i + 1] - ss[l]))
            ans = (ans + v * tot) % MOD  # 累加贡献

        return ans % MOD


if __name__ == '__main__':
    solu = Solution()
    strength = [1, 3, 1, 2]
    print(solu.totalStrength(strength))

    strength = [5, 4, 6]
    print(solu.totalStrength(strength))

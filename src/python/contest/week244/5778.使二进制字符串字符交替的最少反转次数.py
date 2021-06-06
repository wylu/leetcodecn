#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5778.使二进制字符串字符交替的最少反转次数.py
@Time    :   2021/06/06 20:44:02
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
滑动窗口
容易想到令 T = S + S，然后使用滑动窗口的方式来模拟操作一。

我们的目标串是 01...01 或 10...10，而操作二的所需次数，实际上就是原串与目标串
相异的位置的数目。因此，我们令 T1 为 '01'*n，T2 为 '10'*n，然后在滑动窗口的
过程中维护原串与这两个目标串的相异位置数即可。
"""


class Solution:
    def minFlips(self, s: str) -> int:
        ans = n = len(s)
        t = s + s
        a = '01' * n
        b = '10' * n

        ca = cb = 0
        for i in range(n * 2):
            if t[i] != a[i]:
                ca += 1
            if t[i] != b[i]:
                cb += 1
            if i >= n:
                if t[i - n] != a[i - n]:
                    ca -= 1
                if t[i - n] != b[i - n]:
                    cb -= 1
            if i >= n - 1:
                ans = min(ans, ca, cb)

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.minFlips(s="111000"))
    print(solu.minFlips(s="010"))
    print(solu.minFlips(s="1110"))

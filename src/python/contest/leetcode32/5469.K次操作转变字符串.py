#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5469.K次操作转变字符串.py
@Time    :   2020/08/08 22:39:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        cnt = [0] * 26
        for i in range(len(s)):
            delta = (ord(t[i]) - ord(s[i]) + 26) % 26
            cnt[delta] += 1

        hi = 0
        for i in range(1, 26):
            hi = max(hi, (cnt[i] - 1) * 26 + i)

        return hi <= k


# class Solution:
#     def canConvertString(self, s: str, t: str, k: int) -> bool:
#         if len(s) != len(t):
#             return False

#         n = len(s)
#         ans = [0] * n
#         used = {}
#         for i in range(n):
#             if s[i] == t[i]:
#                 continue

#             if s[i] < t[i]:
#                 minOps = ord(t[i]) - ord(s[i])
#             else:
#                 minOps = (ord('z') - ord(s[i])) + (ord(t[i]) - ord('a')) + 1

#             cnt = used.get(minOps, 0)
#             ans[i] = minOps + cnt * 26
#             if ans[i] > k:
#                 return False
#             used[minOps] = cnt + 1

#         return True

if __name__ == '__main__':
    solu = Solution()
    print(solu.canConvertString('aab', 'bbb', 27))
    print(solu.canConvertString('input', 'ouput', 9))
    print(solu.canConvertString('abc', 'bcd', 10))

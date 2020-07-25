#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5458.字符串的好分割数目.py
@Time    :   2020/07/25 22:59:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def numSplits(self, s: str) -> int:
        p, tot = [0] * 26, [0] * 26
        left, right = 0, 0
        for ch in s:
            idx = ord(ch) - ord('a')
            tot[idx] += 1
            if tot[idx] == 1:
                right += 1

        ans = 0
        for ch in s:
            idx = ord(ch) - ord('a')
            p[idx] += 1
            if p[idx] == 1:
                left += 1
            if p[idx] == tot[idx]:
                right -= 1
            if left == right:
                ans += 1

        return ans


# class Solution:
#     def numSplits(self, s: str) -> int:
#         n = len(s)
#         lcnt, rcnt = [], []

#         lcur, rcur = {}, {}
#         for i in range(n):
#             if s[i] in lcur:
#                 lcur[s[i]] += 1
#             else:
#                 lcur[s[i]] = 1
#             lcnt.append({k: v for k, v in lcur.items()})

#             if s[n - 1 - i] in rcur:
#                 rcur[s[n - 1 - i]] += 1
#             else:
#                 rcur[s[n - 1 - i]] = 1
#             rcnt.append({k: v for k, v in rcur.items()})

#         ans = 0
#         for i in range(1, n):
#             if len(lcnt[i - 1]) == len(rcnt[n - 1 - i]):
#                 ans += 1

#         return ans

if __name__ == '__main__':
    solu = Solution()
    print(solu.numSplits('aacaba'))
    print(solu.numSplits('abcd'))
    print(solu.numSplits('aaaaa'))
    print(solu.numSplits('acbadbaada'))

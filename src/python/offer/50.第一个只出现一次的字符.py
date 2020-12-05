#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   50.第一个只出现一次的字符.py
@Time    :   2020/12/05 22:15:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def firstUniqChar(self, s: str) -> str:
        start = {}
        for i in range(len(s)):
            if s[i] in start:
                start[s[i]][1] += 1
            else:
                start[s[i]] = [i, 1]

        ans = [len(s), ' ']
        for k, v in start.items():
            if v[1] == 1 and v[0] < ans[0]:
                ans[0], ans[1] = v[0], k

        return ans[1]


if __name__ == "__main__":
    solu = Solution()
    print(solu.firstUniqChar("abaccdeff"))
    print(solu.firstUniqChar(""))
    print(solu.firstUniqChar("aabbcc"))

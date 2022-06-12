#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6094.公司命名.py
@Time    :   2022/06/12 11:49:11
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def distinctNames(self, ideas: List[str]) -> int:
        seen = set(ideas)

        cnt = [[0] * 26 for _ in range(26)]
        for idea in ideas:
            word = list(idea)
            pc = word[0]
            for i in range(26):
                word[0] = nc = chr(ord('a') + i)
                idea = ''.join(word)
                if idea not in seen:
                    cnt[ord(pc) - ord('a')][ord(nc) - ord('a')] += 1

        ans = 0
        for i in range(26):
            for j in range(26):
                ans += cnt[i][j] * cnt[j][i]

        return ans


if __name__ == '__main__':
    solu = Solution()
    ideas = ["coffee", "donuts", "time", "toffee"]
    print(solu.distinctNames(ideas))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5834.使用特殊打字机键入单词的最少时间.py
@Time    :   2021/08/21 22:30:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 0
        cur = 0
        for ch in word:
            target = ord(ch) - ord('a')
            if target > cur:
                ans += min(target - cur, 26 - (target - cur))
            elif target < cur:
                ans += min(cur - target, 26 - (cur - target))
            cur = target
            ans += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.minTimeToType("abc"))
    print(solu.minTimeToType("bza"))
    print(solu.minTimeToType("zjpc"))

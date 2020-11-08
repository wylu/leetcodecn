#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5562.字符频次唯一的最小删除次数.py
@Time    :   2020/11/08 10:43:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def minDeletions(self, s: str) -> int:
        cnts = [0] * 26
        for ch in s:
            cnts[ord(ch) - ord('a')] += 1

        ans, exist = 0, set()
        for cnt in cnts:
            if cnt != 0:
                i, tmp = 0, cnt
                while tmp > 0 and tmp in exist:
                    i += 1
                    tmp = cnt - i
                ans += i
                exist.add(tmp)
        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.minDeletions('aab'))
    print(solu.minDeletions('aaabbbcc'))
    print(solu.minDeletions('ceabaacb'))

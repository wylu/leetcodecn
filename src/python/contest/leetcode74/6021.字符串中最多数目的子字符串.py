#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6021.字符串中最多数目的子字符串.py
@Time    :   2022/03/19 22:35:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        a, b = pattern[0], pattern[1]
        s2 = [ch for ch in text if ch in pattern]
        s1 = [a]
        s1.extend(s2)
        s2.append(b)

        if a == b:
            n = len(s1) - 1
            return (1 + n) * n // 2

        def count(arr):
            ca = cb = 0
            for ch in arr:
                if ch == a:
                    ca += 1
                else:
                    cb += 1

            res = 0
            for ch in arr:
                if ch == a:
                    res += cb
                else:
                    cb -= 1

            return res

        return max(count(s1), count(s2))


if __name__ == '__main__':
    solu = Solution()
    print(solu.maximumSubsequenceCount(text="abdcdbc", pattern="ac"))
    print(solu.maximumSubsequenceCount(text="aabb", pattern="ab"))
    print(solu.maximumSubsequenceCount(text="aaaa", pattern="aa"))
    print(solu.maximumSubsequenceCount(text="abab", pattern="ab"))

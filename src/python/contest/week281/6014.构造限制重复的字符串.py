#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6014.构造限制重复的字符串.py
@Time    :   2022/02/20 10:48:02
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnts, total = [0] * 26, 0
        for ch in s:
            cnts[ord(ch) - ord('a')] += 1
            total += 1

        ans, cur = [], 0
        while total:
            for i in range(25, -1, -1):
                if cnts[i] == 0:
                    continue

                ch = chr(i + ord('a'))
                if ans and ans[-1] == ch and cur == repeatLimit:
                    continue

                if ans and ans[-1] != ch:
                    cur = 0

                ans.append(ch)
                cnts[i] -= 1
                cur += 1
                break

            total -= 1

        return ''.join(ans)


if __name__ == '__main__':
    solu = Solution()
    print(solu.repeatLimitedString(s="cczazcc", repeatLimit=3))
    print(solu.repeatLimitedString(s="aababab", repeatLimit=2))

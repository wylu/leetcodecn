#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5754.长度为三且各字符不同的子字符串.py
@Time    :   2021/05/29 22:30:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 2):
            if len(set(list(s[i:i + 3]))) == 3:
                ans += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.countGoodSubstrings(s="xyzzaz"))
    print(solu.countGoodSubstrings(s="aababcabc"))

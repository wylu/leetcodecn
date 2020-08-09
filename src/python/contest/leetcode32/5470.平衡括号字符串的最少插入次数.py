#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5470.平衡括号字符串的最少插入次数.py
@Time    :   2020/08/08 23:12:08
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        if not s:
            return 0

        ans = 0
        left, i, n = 0, 0, len(s)
        while i < n:
            if s[i] == '(':
                left += 1
            else:
                if left > 0:
                    if i < n - 1 and s[i + 1] == ')':
                        i += 1
                    else:
                        ans += 1
                    left -= 1
                else:
                    if i < n - 1 and s[i + 1] == ')':
                        ans += 1
                        i += 1
                    else:
                        ans += 2
            i += 1

        ans += left * 2

        return ans


# class Solution:
#     def minInsertions(self, s: str) -> int:
#         if not s:
#             return 0

#         ans = 0
#         left, i, n = 0, 0, len(s)
#         while i < n:
#             if s[i] == '(':
#                 left += 1
#                 i += 1
#                 continue

#             if left > 0:
#                 if i < n - 1 and s[i + 1] == ')':
#                     left -= 1
#                     i += 2
#                 else:
#                     left -= 1
#                     ans += 1
#                     i += 1
#             else:
#                 if i < n - 1 and s[i + 1] == ')':
#                     i += 2
#                     ans += 1
#                 else:
#                     i += 1
#                     ans += 2

#         ans += left * 2

#         return ans

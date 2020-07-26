#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5473.灯泡开关IV.py
@Time    :   2020/07/26 10:34:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def minFlips(self, target: str) -> int:
        target = '0' + target
        ans = 0
        for i in range(1, len(target)):
            if target[i] != target[i - 1]:
                ans += 1
        return ans


# """
# 0            0*2
# 01           1*2-1
# 10           1*2
# 101          2*2-1
# 1010         2*2
# 10101        3*2-1
# 101010       3*2
# ...
# """

# class Solution:
#     def minFlips(self, target: str) -> int:
#         cnt = 1 if target[0] == '1' else 0
#         for i in range(1, len(target)):
#             if target[i] == '1' and target[i - 1] == '0':
#                 cnt += 1

#         ans = 2 * cnt
#         return ans if target[-1] == '0' else ans - 1

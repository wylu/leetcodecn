#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5723.查找用户活跃分钟数.py
@Time    :   2021/04/04 10:32:17
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]],
                                  k: int) -> List[int]:
        user2minu = defaultdict(set)
        for user, minu in logs:
            user2minu[user].add(minu)

        ans = [0] * k
        for val in user2minu.values():
            ans[len(val) - 1] += 1

        return ans

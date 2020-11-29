#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5613.最富有客户的资产总量.py
@Time    :   2020/11/29 10:30:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(ac) for ac in accounts)

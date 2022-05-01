#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6048.必须拿起的最小连续卡牌数.py
@Time    :   2022/05/01 10:36:29
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = len(cards) + 1
        indices = {}
        for i, card in enumerate(cards):
            if card in indices:
                ans = min(ans, i - indices[card] + 1)
            indices[card] = i
        return -1 if ans == len(cards) + 1 else ans

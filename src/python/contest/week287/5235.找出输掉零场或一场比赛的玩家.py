#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5235.找出输掉零场或一场比赛的玩家.py
@Time    :   2022/04/03 10:41:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        counter = defaultdict(int)
        for winner, loser in matches:
            counter[loser] += 1
            players.add(winner)
            players.add(loser)

        ans = [[], []]
        for player in sorted(players):
            if not counter[player]:
                ans[0].append(player)
            elif counter[player] == 1:
                ans[1].append(player)

        return ans
